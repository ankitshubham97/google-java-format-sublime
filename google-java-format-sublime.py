import sublime, sublime_plugin
import subprocess
import sys

class GoogleJavaFormatCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		p = subprocess.Popen(['java', '-jar', './artifacts/google-java-format-1.8-SNAPSHOT-all-deps.jar', '-i', str(self.view.file_name())], stdout=subprocess.PIPE, stderr=None, stdin=None)
		stdout, stderr = p.communicate()
		if p.returncode != 0:
			sys.exit(p.returncode)
