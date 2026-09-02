%% run_preprocess.m - fMRI 预处理主脚本（模板）
%  功能：SPM25 + CAT12 + DPABI 批量预处理
%  用法：修改下方配置后运行
%  依赖：SPM25、CAT12、DPABI 已加入 MATLAB 路径

%% ==================== 配置区（软编码，置顶） ====================
ROOT_DIR    = 'F:\SSD';          % 根目录，每个一级子文件夹为一个被试
BOLD_KEY    = 'bold';            % 功能像关键词
T1_KEY      = 'mprage';          % 结构像关键词
TR          = 3;                 % 重复时间（秒）
NSLICES     = 36;                % 切片数
FWHM        = 6;                 % 平滑核（mm）
ATLAS_FILE  = 'F:\matlab\AAL3_1mm.nii';  % Atlas 文件（后处理用）
SKIP_EXIST  = true;              % 是否跳过已有中间文件（断点续传）
%% ================================================================

%% 获取被试列表
subjects = dir(ROOT_DIR);
subjects = subjects([subjects.isdir] & ~startsWith({subjects.name}, '.'));
fprintf('发现 %d 个被试\n', numel(subjects));

%% 逐个处理（并行版见 parallel_preprocess.m）
for i = 1:numel(subjects)
    subj_dir = fullfile(ROOT_DIR, subjects(i).name);
    fprintf('\n===== [%d/%d] 处理被试 %s =====\n', i, numel(subjects), subjects(i).name);
    try
        process_subject(subj_dir, BOLD_KEY, T1_KEY, TR, NSLICES, FWHM, SKIP_EXIST);
    catch ME
        fprintf('❌ 被试 %s 处理失败: %s\n', subjects(i).name, ME.message);
        continue;  % 单个失败不中断
    end
end
fprintf('\n✅ 全部处理完成\n');

%% ==================== 子函数 ====================
function process_subject(subj_dir, BOLD_KEY, T1_KEY, TR, NSLICES, FWHM, SKIP_EXIST)
    % 查找功能像与结构像
    bold_file = find_file(subj_dir, BOLD_KEY);
    t1_file   = find_file(subj_dir, T1_KEY);
    if isempty(bold_file)
        error('未找到功能像（关键词: %s）', BOLD_KEY);
    end

    % [Step 2] 时层校正（若未完成）
    a_file = ['a' bold_file];
    if SKIP_EXIST && exist(a_file, 'file')
        fprintf('  ⏭️ 时层校正已存在，跳过\n');
    else
        fprintf('  🔄 时层校正...\n');
        % 此处调用 spm_slice_timing
        % spm_slice_timing({bold_file}, slice_order, TR);
    end

    % [Step 3] 头动校正
    ra_file = ['ra' bold_file];
    if SKIP_EXIST && exist(ra_file, 'file')
        fprintf('  ⏭️ 头动校正已存在，跳过\n');
    else
        fprintf('  🔄 头动校正...\n');
        % 此处调用 spm_realign
    end

    % [Step 4] 配准
    % [Step 5] 标准化（CAT12）
    % [Step 6] 平滑
    % [Step 7] 时间去噪与一阶分析
    fprintf('  ✅ 被试处理完成\n');
end

function f = find_file(dir_path, keyword)
    % 在目录中查找包含关键词的文件
    files = dir(fullfile(dir_path, ['*' keyword '*']));
    files = files(~[files.isdir]);
    if isempty(files)
        f = '';
    else
        f = fullfile(dir_path, files(1).name);
    end
end