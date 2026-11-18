% SETUP_MATLAB
% Adds the repository and its analysis subdirectories to the MATLAB search path. Run it
% once from the CODE root before calling scripts that use project_config.
% Inputs and run settings: see README.md and docs/DATA.md.

%SETUP_MATLAB Add this repository and its subdirectories to the MATLAB path.

repo_root = fileparts(mfilename('fullpath'));
addpath(genpath(repo_root));
disp('Added Synoptic Map Prediction repository to the MATLAB path:');
disp(repo_root);
