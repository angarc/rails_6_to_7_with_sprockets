import re
import subprocess
from .file_helpers import replace_line_in_file, add_to_file

def run_pipeline():
  gemfile_path = "./Gemfile"

  update_rails_version(gemfile_path)
  update_bootstrap_version(gemfile_path)
  add_sprockets_gem(gemfile_path)
  bundle_update()

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

def add_sprockets_gem(gemfile_path):
  add_to_file(
    gemfile_path, 
    re.compile('gem [\'"]sprockets-rails[\'"]'),
    "gem 'sprockets-rails'\n"
  )

def bundle_update():
  p = subprocess.Popen(['bundle', 'update'], bufsize=2048, stdin=subprocess.PIPE)
  p.wait()

  if p.returncode == 0:
    print("bundle updated")
  else:
    print("bundle update failed")

def bundle_install():
  p = subprocess.Popen(['bundle', 'install'], bufsize=2048, stdin=subprocess.PIPE)
  p.wait()

  if p.returncode == 0:
    print("bundle installed")
  else:
    print("bundle install failed")