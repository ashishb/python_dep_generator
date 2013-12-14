#!/usr/bin/python
import argparse
import importlib
import inspect
import logging
import os
import sys
import traceback
import types


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


class DepGenerator(object):

	def __init__(self):
		# Maps a module (filename) to set of module (filenames) its dependent on.
		self._dependency_dict = {}

	def generateDepGraph(self, path):
		assert path, 'path must be provided.' 
		assert os.path.exists(path), 'path %s must refer to file/dir.' % path
		if os.path.isdir(path):
			logger.debug('path %s is dir.', path)
			for filename in os.listdir(path):
				self.generateDepGraph(os.path.join(path, filename))
		else:
			if path.endswith('.py'):
				self._GenerateDepGraphForOnePyFile(path)
		return self._dependency_dict

	def _GenerateDepGraphForOnePyFile(self, path):
		if self._dependency_dict.get(path, None) is None:
			self._dependency_dict[path] = set()
		base_path = os.path.dirname(os.path.abspath(path))
		module_name = os.path.basename(path)[:-3]
		sys.path.append(base_path)
		try:
			module = importlib.import_module(module_name)
			for (member_name, member_obj) in inspect.getmembers(module):
				if type(member_obj) == types.ModuleType:
					if hasattr(member_obj, '__file__') and not (
							# I wish I had a better way to do this.
							member_obj.__file__.startswith('/usr/')):
							dependency = member_obj.__file__.replace('.pyc', '.py')
					else:
							dependency = member_name
					self._dependency_dict[path].add(dependency)
		except ImportError as e:
			logger.error('Failed to import %s', path)
		except Exception as e:
			logger.error('Error happened while importing %s', path)

	@staticmethod
	def prettyPrint(dep_dict, hide_system_packages=False):
		for (k, deps) in dep_dict.items():
			if len(deps):
				print 
				print k
				for dep in sorted(deps):
					if not hide_system_packages or dep.startswith('/'):
						print '|_', dep


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument(dest='path',
			help='path (or dir) of the python file (or all python files under it).')
	parser.add_argument('-s', '--small_list', action='store_true', default=False,
			help='Pass -s to hide '
			'system	packages and get a smaller list.')
	args = parser.parse_args()
	dep_dict = DepGenerator().generateDepGraph(args.path)
	DepGenerator.prettyPrint(dep_dict, hide_system_packages=args.small_list)


if __name__ == '__main__':
	main()
