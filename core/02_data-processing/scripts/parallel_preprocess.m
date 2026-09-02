%% parallel_preprocess.m - fMRI 预处理并行脚本（模板）
%  功能：使用并行计算（parfor）处理多个被试
%  用法：修改下方配置后运行
%  依赖：SPM25、CAT12、DPABI、Parallel Computing Toolbox

%% ==================== 配置区（软编码，置顶） ====================
ROOT_DIR     = 'F:\SSD';     % 根目录
BOLD_KEY     = 'bold';       % 功能像关键词
T1_KEY       = 'mprage';     % 结构像关键词
TR           = 3;            % 重复时间
NSLICES      = 36;           % 切片数
FWHM         = 6;            % 平滑核
NUM_WORKERS  = 4;            % 并行工作进程数
USE_GPU      = false;        % 是否使用 GPU（CAT12 可走 GPU）
SKIP_EXIST   = true;         % 跳过已有中间文件
%% ================================================================

%% 获取被试列表
subjects = dir(ROOT_DIR);
subjects = subjects([subjects.isdir] & ~startsWith({subjects.name}, '.'));
fprintf('发现 %d 个被试，启动 %d 个并行进程\n', numel(subjects), NUM_WORKERS);

%% 启动并行池
if isempty(gcp('nocreate'))
    parpool('local', NUM_WORKERS);
end

%% 并行处理
parfor i = 1:numel(subjects)
    subj_dir = fullfile(ROOT_DIR, subjects(i).name);
    fprintf('===== [%d/%d] 处理被试 %s =====\n', i, numel(subjects), subjects(i).name);
    try
        process_subject(subj_dir, BOLD_KEY, T1_KEY, TR, NSLICES, FWHM, SKIP_EXIST);
    catch ME
        % 并行中不中断其他被试
        fprintf('❌ 被试 %s 处理失败: %s\n', subjects(i).name, ME.message);
    end
end

%% 关闭并行池
delete(gcp('nocreate'));
fprintf('\n✅ 全部处理完成\n');

%% ==================== 子函数 ====================
function process_subject(subj_dir, BOLD_KEY, T1_KEY, TR, NSLICES, FWHM, SKIP_EXIST)
    bold_file = find_file(subj_dir, BOLD_KEY);
    if isempty(bold_file)
        error('未找到功能像（关键词: %s）', BOLD_KEY);
    end

    % 各步骤均检查中间文件，支持断点续传
    a_file = ['a' bold_file];
    if SKIP_EXIST && exist(a_file, 'file')
        fprintf('  ⏭️ 时层校正已存在，跳过\n');
    else
        fprintf('  🔄 时层校正...\n');
        % spm_slice_timing({bold_file}, slice_order, TR);
    end

    ra_file = ['ra' bold_file];
    if SKIP_EXIST && exist(ra_file, 'file')
        fprintf('  ⏭️ 头动校正已存在，跳过\n');
    else
        fprintf('  🔄 头动校正...\n');
        % spm_realign
    end

    % [Step 4-7] 配准、标准化（CAT12）、平滑、时间去噪
    fprintf('  ✅ 被试处理完成\n');
end

function f = find_file(dir_path, keyword)
    files = dir(fullfile(dir_path, ['*' keyword '*']));
    files = files(~[files.isdir]);
    if isempty(files)
        f = '';
    else
        f = fullfile(dir_path, files(1).name);
    end
end