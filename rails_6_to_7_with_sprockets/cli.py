import re
from .file_helpers import replace_line_in_file

def run_pipeline():
  gemfile_path = "./Gemfile"

  update_rails_version(gemfile_path)
  update_bootstrap_version(gemfile_path)

def update_rails_version(gemfile_path):
  replace_line_in_file(
    gemfile_path, 
    re.compile('gem [\'"]rails[\'"]'), 
    "gem 'rails', '7.0.4.3'\n"
  )

def update_bootstrap_version(gemfile_path):
  replace_line_in_file(
    gemfile_path,
    re.compile('gem [\'"]bootstrap[\'"]'),
    "gem 'bootstrap', '~> 4.5'\n"
  )
