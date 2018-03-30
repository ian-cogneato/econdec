%% Modified by Richard Bowen from iCount ver. by Christina Gancayco
%  EconDec data merge
%  Last updated 02-24-16 RB
%               03-07-16 ID

%% PARAMETERS %%
clear; %clc;
EstDiffThreshold = 0.521016835270974;

output = [];
%% Load concatenated data

if ~exist(['CONCATclean_EconDec_task_',date,'.xlsx'],'file')
    taskFile=uigetfile('CONCATclean_EconDec_task_*.xlsx','Select task data file');
    [~,~,taskData] = xlsread(taskFile);
else [~,~,taskData] = xlsread(['CONCATclean_EconDec_task_',date,'.xlsx']);
end

if ~exist(['CONCATclean_EconDec_frac_',date,'.xlsx'],'file')
    fracFile=uigetfile('CONCATclean_EconDec_frac_*.xlsx','Select fractal memory file');
    [~,~,fracData] = xlsread(fracFile);
else [~,~,fracData] = xlsread(['CONCATclean_EconDec_frac_',date,'.xlsx']);
end

if ~exist(['CONCATclean_EconDec_face_',date,'.xlsx'],'file')
    faceFile=uigetfile('CONCATclean_EconDec_face_*.xlsx','Select face memory file');
    [~,~,faceData] = xlsread(faceFile);
else [~,~,faceData] = xlsread(['CONCATclean_EconDec_face_',date,'.xlsx']);
end

%% cleanup


oldheaders = taskData(1,1:34);

taskData = taskData(2:end,1:34);
fracData = fracData(2:end,:);
faceData = faceData(2:end,:);

% Sort data by subject
taskData = sortrows(taskData,1);
fracData = sortrows(fracData,1);
faceData = sortrows(faceData,1);

% Separate into individual subject arrays
taskSub = cell2mat(taskData(:,1)); [~,~,taskIdx] = unique(taskSub);
fracSub = cell2mat(fracData(:,1)); [~,~,fracIdx] = unique(fracSub);
faceSub = cell2mat(faceData(:,1)); [~,~,faceIdx] = unique(faceSub);

orgTask = mat2cell(taskData,accumarray(taskIdx(:),1),34);
orgFrac = mat2cell(fracData,accumarray(fracIdx(:),1),11);
orgFace = mat2cell(faceData,accumarray(faceIdx(:),1),10);

%% Add fractal and face memory data to task data

for n = 1:length(orgTask)
    
    subTask = orgTask{n};
    subFrac = orgFrac{n};
    subFace = orgFace{n};
    
    oldfrac = subFrac(:,8);
    face = subFace(:,7);
    
    % to add outlier checking, need to expand cols. below
    stockData = cell(length(subTask),2);
    bondData = cell(length(subTask),2);
    faceData = cell(length(subTask),2);
    
    for j = 1:6:length(subTask)
        stockpic = subTask{j,13};
        bondpic = subTask{j,14};
        
        stockIdx = [];
        bondIdx = [];
        
        for pp = 1:length(oldfrac)
            stockIdx = [stockIdx;strcmp(stockpic,oldfrac{pp})];
            bondIdx = [bondIdx;strcmp(bondpic,oldfrac{pp})];
        end
        
        stockIdx = find(stockIdx);
        bondIdx = find(bondIdx);
        
        if ~isempty(stockIdx) && ~isempty(bondIdx)
            stockData(j,:) = subFrac(stockIdx,9:10);
            % need to calculate for stock outliers here
            % check to see if current BondMem data is empty
                % if isEmpty(stockData{j,1})
                    % stockData{j,3} = [];
                % else
                    % if (stockData{j,2} > 0.5) && (stockData{j,2} < 29.6948066714155)
                % stockData(j,3)
            bondData(j,:) = subFrac(bondIdx,9:10);
            % need to calculate for bond outliers here
        else
            stockData(j,:) = {'ERROR','ERROR'};
            bondData(j,:) = {'ERROR','ERROR'};
        end
    end
    
    for k = 1:length(subTask)
        facepic = subTask{k,20};
        
        faceIdx = [];
        
        for qq = 1:length(face)
            faceIdx = [faceIdx;strcmp(facepic,face{qq})];
        end
        
        faceIdx = find(faceIdx);
        
        if ~isempty(faceIdx)
            faceData(k,:) = subFace(faceIdx,9:10);
        else faceData(k,:) = {'ERR'};
        end
        % need to calculate for face outliers here
    end
    
    output = [output;subTask,bondData,stockData,faceData];
    
  % 
    
end

headers = {'BondMem','BondMemRT' ... % CBondMemRT
         'StockMem','StockMemRT' ... % CStockMemRT
         'FaceMem','FaceMemRT' ...   % CFaceMemRT
         'StockPickedYes', 'EstDiff' ...
         'CEstDiff', 'ProbB4choice', 'B4choiceProb', 'CodedOutcome'};
     

headers = [oldheaders,headers];

%% add additional calculated data to output, under new headers

%% CHANGE INDEXING - EVALUATE (F9) taskData array creation line at the top of program for proper indices
pre_concat_output = [];
numRows = size(output,1);
StockPicked = cell(numRows,1);
    for n = 1:numRows
        if strcmp(taskData{n,15}, 'stock')
            StockPicked{n,1} = 1;
        else
            StockPicked{n,1} = 0;
        end
    end
%       // EstDiff = abs((col23*0.01)-col33)
%       // col23 is ProbGood and col33 is TrueProbGood
EstDiff = taskData(1:end, 23:23);
       for n = 1:length(StockPicked)
           EstDiff{n} = abs((EstDiff{n}*0.01) - taskData{n, 33});
       end
CEstDiff = cell(numRows,1);
       for n = 1:length(StockPicked)
           if EstDiff{n} < EstDiffThreshold   %Need 2 know if thres chang
               CEstDiff{n} = 1;
           else
               CEstDiff{n} = 0;
           end
       end
ProbB4choice = cell(numRows,1);
       for n = 1:length(StockPicked)
           if taskData{n,7} == 1   %taskData_col7 is TrialNum
               ProbB4choice{n} = 0.5;
           else
               ProbB4choice{n} = taskData{n,33};
           end
       end
B4choiceProb = cell(numRows,1);
       for n = 1:length(StockPicked)
           if ProbB4choice{n} > 0.5
               B4choiceProb{n} = 1;
           else
               if ProbB4choice{n} < 0.5
                   B4choiceProb{n} = -1;
               else
                   B4choiceProb{n} = 0;
               end
           end
       end
CodedOutcome = cell(numRows,1);
       for n = 1:length(StockPicked)
           if taskData{n,33} > 0.5
               CodedOutcome{n} = 1;
           else
               if taskData{n,33} < 0.5
                   CodedOutcome{n} = -1;
               else
                   CodedOutcome{n} = 0;
               end
           end
       end
% pre_concat_output = [StockPicked, EstDiff, CEstDiff, ...
%                       ProbB4choice, B4choiceProb, CodedOutcome];

% newheaders = {'StockPickedYes', 'EstDiff', 'CEstDiff', ...
%       'ProbB4choice', 'B4choiceProb', 'CodedOutcome'};

% pre_concat_output = [newheaders;pre_concat_output];
% xlswrite('iCount_RTBmerge.xlsx', pre_concat_output);
%% above is end of RTB edits
output = [output, StockPicked, EstDiff, CEstDiff, ProbB4choice, ...
               B4choiceProb, CodedOutcome];
output = [headers;output];


xlswrite(['CONCATmerge_EconDec_',date,'.xlsx'],output)