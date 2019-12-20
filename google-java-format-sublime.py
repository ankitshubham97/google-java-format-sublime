import sublime, sublime_plugin
import subprocess
import sys

class GoogleJavaFormatCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		file_name = self.view.file_name()
		if file_name is None:
			return
		p = subprocess.Popen(['java', '-jar', sublime.packages_path()+'/GoogleJavaFormatter/artifacts/google-java-format-1.8-SNAPSHOT-all-deps.jar', '-i', self.view.file_name()], stdout=subprocess.PIPE, stderr=None, stdin=None)
		stdout, stderr = p.communicate()
		if p.returncode != 0:
			sys.exit(p.returncode)
