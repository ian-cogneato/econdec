%% New EconDec data concatenation
%   Ian AD 03-07-16
%   Prepares EconDec subject datafiles for merging and preprocessing
%   
%   Be sure to change offset parameter depending on your data series:

offset=200; %99 for 100-series, 200 for 201-series

%% Identify existing files in the directory to be concatenated 

dirlist = dir; fNames=[];
taskFiles=[]; fracFiles=[]; faceFiles=[];

for i=1:length(dirlist)
    if length(dirlist(i).name) >= 6
        if strcmp( dirlist(i).name(end-4:end), '.xlsx')
            fNames{end+1,1}=dirlist(i).name;
        end
    end
end

for i=1:length(fNames)
    ser = fNames{i}(8:11);
    if strcmp(ser,'task')
        taskFiles{end+1,1} = fNames{i};
    elseif strcmp(ser,'frac')
        fracFiles{end+1,1} = fNames{i};
    elseif strcmp(ser,'face')
        faceFiles{end+1,1} = fNames{i};
    end
end

%% Read in and concatenate three data series

[~,~,taskData] = xlsread(taskFiles{1});
taskDummy = num2cell(ones(size(taskData(2:end,:))));
taskData = taskData(1,1:end);

[~,~,fracData] = xlsread(fracFiles{1});
fracDummy = num2cell(ones(size(fracData(2:end,:))));
fracData = fracData(1,1:end);

[~,~,faceData] = xlsread(faceFiles{1});
faceDummy = num2cell(ones(size(faceData(2:end,:))));
faceData = faceData(1,1:end);

disp('Task data...');
i=1;
while i <= length(taskFiles)
    if strcmp(taskFiles{i}(13:15),num2str(i+offset))
        fprintf(['ss#',num2str(i+offset)]);
        [~,~,fileData] = xlsread(taskFiles{i});
        fileData = fileData(2:end,:);
        taskData = [taskData;fileData];
        if fileData{1,1}==i+offset, fprintf(' good\n'); 
        else fprintf([' mismatch: ',num2str(fileData{1,1}),'\n']); break;
        end
    else
        disp(['ss#', num2str(i+offset),' missing']);
        taskFiles(i+1:end+1) = taskFiles(i:end); taskFiles{i}='';
        taskDummy(:,1) = num2cell(i+offset);
        taskData = [taskData;taskDummy];
    end
    i=i+1;
end
disp('Done.');

disp('Frac data...');
i=1;
while i <= length(fracFiles)
    if strcmp(fracFiles{i}(19:21),num2str(i+offset))
        disp(['ss#',num2str(i+offset),' good']);
        [~,~,fileData] = xlsread(fracFiles{i});
        fileData = fileData(2:end,:);
        fracData = [fracData;fileData];
    else
        disp(['ss#', num2str(i+offset),' missing']);
        fracFiles(i+1:end+1)=fracFiles(i:end); fracFiles{i}='';
        fracDummy(:,1) = num2cell(i+offset);
        fracData = [fracData;fracDummy];
    end
    i=i+1;
end
disp('Done.');

disp('Face data...');
i=1;
while i <= length(faceFiles)
    if strcmp(faceFiles{i}(19:21),num2str(i+offset))
        disp(['ss#',num2str(i+offset),' good']);
        [~,~,fileData] = xlsread(faceFiles{i});
        fileData = fileData(2:end,:);
        faceData = [faceData;fileData];
    else
        disp(['ss#', num2str(i+offset),' missing']);
        faceFiles(i+1:end+1)=faceFiles(i:end); faceFiles{i}='';
        faceDummy(:,1) = num2cell(i+offset);
        faceData = [faceData;faceDummy];
    end
    i=i+1;
end
disp('Done.');

%% Output concatenated data to Excel, ready for merging

fprintf('Writing.');
xlswrite(['CONCATclean_EconDec_task_',date,'.xlsx'],taskData); fprintf('.');
xlswrite(['CONCATclean_EconDec_frac_',date,'.xlsx'],fracData); fprintf('.');
xlswrite(['CONCATclean_EconDec_face_',date,'.xlsx'],faceData); fprintf(' Done!\n\n');