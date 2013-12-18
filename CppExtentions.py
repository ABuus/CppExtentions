import sublime, sublime_plugin
import os.path
import io

#
# BASENAMEUPPER replaced with filename in upprecase
# BASENAME replaced with filename 
#

header_solo = """#ifndef BASENAMEUPPER_H_INC
#define BASENAMEUPPER_H_INC


#endif // BASENAMEUPPER_H_INC

"""

class_header = """#ifndef BASENAMEUPPER_H_INC
#define BASENAMEUPPER_H_INC

class BASENAME
{
public:
	BASENAME();
	virtual ~BASENAME();
};

#endif // BASENAMEUPPER_H_INC

"""

class_source = """#include \"BASENAME.h\"

BASENAME::BASENAME()
{}

BASENAME::~BASENAME()
{}

"""

class NewCppHeaderCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		self.path = "".join(paths)
		reply = self.window.show_input_panel("Header Name (Without extention):", "", self.on_completed, None, None)

	def is_enabled(self, paths = []):
		return os.path.isdir("".join(paths))

	def on_completed(self, basename):
		absName = self.path + "/" + basename + ".h"
		if not os.path.exists(absName):
			f = open(absName, 'w')
			f.write(header_solo.replace("BASENAMEUPPER", basename.upper()).replace("BASENAME", basename))
			f.close()
		self.window.open_file(absName)

class NewCppClassCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		self.path = "".join(paths)
		reply = self.window.show_input_panel("Class Name:", "", self.on_completed, None, None)

	def is_enabled(self, paths = []):
		return os.path.isdir("".join(paths))

	def on_completed(self, basename):
		absHeaderName = self.path + "/" + basename + ".h"
		if not os.path.exists(absHeaderName):
			f = open(absHeaderName, 'w')
			f.write(class_header.replace("BASENAMEUPPER", basename.upper()).replace("BASENAME", basename))
			f.close()
		self.window.open_file(absHeaderName)

		absSourceName = self.path + "/" + basename + ".cpp"
		if not os.path.exists(absSourceName):
			f = open(absSourceName, 'w')
			f.write(class_source.replace("BASENAMEUPPER", basename.upper()).replace("BASENAME", basename))
			f.close()
		self.window.open_file(absSourceName)
	
		