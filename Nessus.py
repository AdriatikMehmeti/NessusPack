#!/bin/python3
import sys,os
from time import sleep
from EmailManage import EmailManage
from Sys import Sys as System

class Nessus:

	def __init__(self):
		# Basic Info
		self.tool = 'Nessus'
		self.type = 'expert'.upper()
		self.version = '10.3 or later'
		self.Author = 'Adriatik a.k.a'
		self.Repo = 'github.com/AdriatikMehmeti/Nessus_pack'
		self.Last_update = '28 Gushte 2022'
		self.Title = self.tool + 'Pack'

		# Text Style and color
		self.text_style ={'HEADER':'\033[95m',
					  'OKBLUE':'\033[94m',
					  'OKCYAN':'\033[96m',
					  'OKGREEN':'\033[92m',
					  'WARNING':'\033[93m',
					  'FAIL':'\033[91m',
					  'ENDC':'\033[0m',
					  'BOLD':'\033[1m',
					  'UNDERLINE':'\033[4m'}
		self.Email = None
		# Paths
		self.backup_path = '/opt/nessus_backup/'
		self.nessus_path = '/opt/nessus/'

	def _banner(self):
		print("{}[#] ============================================================================={} \n"
			"[+] {} \n"
			"[+] Last Update: {} \n"
			"[+] {}Author: {} {} \n"
			"[+] Github: {}{}{}  \n"
			"{}[#] ============================================================================={}\n"
			.format(self.text_style.get('FAIL'),self.text_style.get('ENDC'),self.Title,self.Last_update,
					self.text_style.get('OKGREEN'),self.Author,self.text_style.get('ENDC'),self.text_style.get('BOLD'),
					self.Repo,self.text_style.get('ENDC'),self.text_style.get('FAIL'),self.text_style.get('ENDC')))

	def _Email(self):

		os.system('clear')
		self._banner()

		self.Email = EmailManage()
		self.Email.INIT()
		self.Email.wait_message()
		self.Email.read_message()

		sleep(1)
		input('Press ENTER to continue...')

	def _reset(self, verbose = True):

		os.system('clear')
		self._banner()

		if verbose:
			# Nessus Registeration
			print('\n{}[#] Nessus count RESET {}'.format(self.text_style.get('OKGREEN'),self.text_style.get('ENDC')))

			if os.path.exists('{}var'.format(self.nessus_path)):
				# Removed
				print('\n{}[!] Nessus removed files in process... {}'.format(self.text_style.get('WARNING'),self.text_style.get('ENDC')))
				System('rm -rf {}var'.format(self.nessus_path),'\n{}[+] Nessus removed files successfuly. {}'.format(self.text_style.get('OKGREEN'),self.text_style.get('ENDC'))).run()

			if os.path.exists('{}var'.format(self.backup_path)) and os.path.exists(self.nessus_path[-1]):
				# Writed
				print('\n{}[!] Nessus copied files in process... {}'.format(self.text_style.get('WARNING'), self.text_style.get('ENDC')))
				System('cp -r {}var {}var'.format(self.backup_path,self.nessus_path),'\n{}[+] Nessus copied files successfuly. {}'.format(self.text_style.get('OKGREEN'),self.text_style.get('ENDC'))).run()

		else:
			if os.path.exists('{}var'.format(self.nessus_path)):
				System('rm -rf {}var'.format(self.nessus_path),'').run()
			if os.path.exists('{}var'.format(self.backup_path)) and os.path.exists(self.nessus_path[-1]):
				System('cp -r {}var {}var'.format(self.backup_path,self.nessus_path),'').run()

		sleep(1)
		input('\nPress ENTER to continue...')

	def _backup(self, verbose = True):

		print('\n{}[!] Nessus is going to backup self.'.format(self.text_style.get('WARNING'),self.text_style.get('ENDC')))

		if verbose:

			if os.path.exists(self.backup_path[:-1]):
				System('rm -rf {}'.format(self.backup_path[:-1]),'\n{}[+] Nessus old backup clean successfuly. {}'.format(self.text_style.get('OKGREEN'),self.text_style.get('ENDC'))).run()
			System('cp -r {} {}'.format(self.nessus_path[:-1], self.backup_path[:-1]),'\n{}[+] Nessus backuped successfuly. {}'.format(self.text_style.get('OKGREEN'),self.text_style.get('ENDC'))).run()

		else:
			if os.path.exists(self.backup_path[:-1]):
				System('rm -rf {}'.format(self.backup_path[:-1]),'').run()
			System('cp -r {} {}'.format(self.nessus_path[:-1], self.backup_path[:-1]),'').run()

		sleep(1)

	def _update(self,onlyUpdate = False):

		print('\n{}[!] Nessus is going to update plugins, please do not perform any task in {}. {}'.format(self.text_style.get('WARNING'),
																										   self.tool.upper(),self.text_style.get('ENDC')))
		if onlyUpdate: self._reset(verbose=False);

		System('xterm -e "{}sbin/nessuscli update --all" '.format(self.nessus_path),'').run()

		if onlyUpdate: self._backup(verbose=False);

		sleep(1)

	def _activate(self, verbose = True):

		print('\n{}[#] Nessus Activation {}\n'.format(self.text_style.get('WARNING'), self.text_style.get('ENDC')))
		code = None
		while code is None:
			_code = str(input('Nessus Activation Code: '))
			if len(_code) == 19 and _code.count('-') == 3 :
				code = _code
				del _code

		print('[*] Register process can take few moments.')
		System('xterm -e "{}sbin/nessuscli fetch --register {}"'.format(self.nessus_path,code.upper()),'').run()

		if verbose:
			print('{}[+] Nessus Activate successfuly {}\n'.format(self.text_style.get('OKGREEN'), self.text_style.get('ENDC')))
			sleep(1)
			input('Press ENTER to continue...')

	def _user_manage(self,mode):

		print('\n{}[#] Nessus User Manage {}\n'.format(self.text_style.get('WARNING'), self.text_style.get('ENDC')))

		if mode == 'chpasswd':

			user = str(input('Type User: '))
			#System('{}sbin/nessuscli chpasswd {}'.format(self.nessus_path, user), '{}[+] Nessus user password changed succesfuly. {}\n'.format(self.text_style.get('OKGREEN'),self.text_style.get('ENDC'))).run()
			os.system('{}sbin/nessuscli chpasswd {}'.format(self.nessus_path, user))
		elif mode == 'adduser':

			#System('{}sbin/nessuscli adduser'.format(self.nessus_path),'{}[+] Nessus user added succesfuly. {}\n'.format(self.text_style.get('OKGREEN'),self.text_style.get('ENDC'))).run()
			os.system('{}sbin/nessuscli adduser'.format(self.nessus_path))
		elif mode == 'rmuser':

			#System('{}sbin/nessuscli rmuser'.format(self.nessus_path),'{}[+] Nessus user removed succesfuly. {}\n'.format(self.text_style.get('OKGREEN'),self.text_style.get('ENDC'))).run()
			os.system('{}sbin/nessuscli rmuser'.format(self.nessus_path))
		elif mode == 'lsuser':

			#System('{}sbin/nessuscli lsuser'.format(self.nessus_path), '{}[+] Nessus user listed succesfuly. {}\n'.format(self.text_style.get('OKGREEN'),self.text_style.get('ENDC'))).run()
			os.system('{}sbin/nessuscli lsuser'.format(self.nessus_path))
		sleep(1)
		input('Press ENTER to continue...')

	def _setup(self):

		os.system('clear')
		self._banner()

		print('\n{}[#] Nessus is going to setup env {}\n'.format(self.text_style.get('WARNING'), self.text_style.get('ENDC')))

		# Check if pymailtm is instaled already else install
		try:
			import pymailtm
			del pymailtm
		except Exception as excep:
			del excep
			System('python3 -m pip install pymailtm','{}[+] Python package "pymailtm" installed Successfuly{}'.format(self.text_style.get('OKGREEN'),self.text_style.get('ENDC'))).run()

		# Setup Nessus
		import glob
		file = glob.glob('*.deb')[0]

		if file:
			System('ar -x {}'.format(file),'\n{}[+] Nessus package extracted {}\n'.format(self.text_style.get('OKGREEN'), self.text_style.get('ENDC'))).run()
			System('tar -xf data.tar.gz','\n{}[+] "data.tar.gz" extracted {}\n'.format(self.text_style.get('OKGREEN'), self.text_style.get('ENDC'))).run()
			System('mv opt/nessus /opt/','\n{}[+] Nessus files moved to path: /opt/ {}\n'.format(self.text_style.get('OKGREEN'), self.text_style.get('ENDC'))).run()
			System('rm -rf opt control.tar.gz data.tar.gz Nessus-10.3.0-debian9_amd64.deb debian-binary','\n{}[+] Clean Dir {}\n'.format(self.text_style.get('OKGREEN'), self.text_style.get('ENDC'))).run()

		#del glob

		# Init Activation of Nessus
		self._activate(verbose=False)
		if not os.path.exists(self.backup_path[:-1]):
			System('mkdir {}'.format(self.backup_path[:-1]),'{}[+] Backup path created succesfuly. {}\n'.format(self.text_style.get('OKGREEN'),self.text_style.get('ENDC'))).run()

		# Update Nessus Plugins
		self._update(onlyUpdate=False)
		print('{}[+] Updated succesfuly. {}\n'.format(self.text_style.get('OKGREEN'),self.text_style.get('ENDC')))

		# Backup Nessus
		self._backup(verbose=False)
		print('{}[+] Backuped succesfuly. {}\n'.format(self.text_style.get('OKGREEN'),self.text_style.get('ENDC')))

		System('cp -r ../NessusPack /opt/','{}[+] NessusPack copied succesfuly to path /opt/ . {}\n'.format(self.text_style.get('OKGREEN'),self.text_style.get('ENDC'))).run()

		System('chmod +x /opt/NessusPack/Nessus.py','').run()

		System('echo "#!/bin/bash " > /usr/bin/nessus_extend && echo "/opt/NessusPack/Nessus.py" >> /usr/bin/nessus_extend','{}[+] NessusPack launcher succesfuly created. \n[+] Path: /usr/bin/nessus_extend.\n \nNo you can launch by typing nessus_extend  {}\n'.format(
				self.text_style.get('OKGREEN'),self.text_style.get('ENDC'))).run()

		System('chmod +x /usr/bin/nessus_extend','{}[+] "nessus_extend" change mode executable . {}\n'.format(self.text_style.get('OKGREEN'),self.text_style.get('ENDC'))).run()

		print('\nNext you can run script by typing "nessus_extend". ')

		sleep(1)
		input('Press ENTER to continue...')

	def main(self):

		# Check Role
		if os.geteuid() != 0:
			self._banner()
			sleep(0.5)
			exit('\n{}[*] You need to have root privileges.\n[-] Exiting.{}'.format(self.text_style.get('FAIL'),self.text_style.get('ENDC')))

		# Check Python Version 3
		if int(sys.version.split('.')[0]) != 3:
			self._banner()
			sleep(0.5)
			exit('\n{}[*] Script need to run with Python 3.\n[-] Exiting.{}'.format(self.text_style.get('FAIL'),
																					self.text_style.get('ENDC')))

		while True:
			os.system('clear')
			self._banner()

			answer = None
			option = None

			if len(sys.argv) < 2:
				answer = str(input('{}[#] =================================== Menu ===================================={}{}\n'
								   '[0] Setup Environment   (In case of running this script for first time)\n[1] Nessus Reset Trial\n[2] Nessus Update\n[3] Nessus Backup\n'
								   '[4] Nessus Activation\n[5] Email Service\n[6] Nessus Change Password\n[7] Nessus Add Users\n[8] Nessus Remove Users\n[9] Nessus List Users '
								   '\n[ start ] Nessus Start {}\n'
								   '{}option: {}'.format(self.text_style.get('FAIL'),self.text_style.get('ENDC'),self.text_style.get('OKGREEN'),self.text_style.get('ENDC'),
														 self.text_style.get('FAIL'),self.text_style.get('ENDC'))))

				if answer.isdigit():
					option = int(answer)
					answer = None
			else:
				answer = str(sys.argv[1])


			if option == 0 or answer == '-setup':
				self._setup()
			elif option == 1 or answer == '-reset':
				self._reset()
			elif option == 2 or answer == '-update':
				self._update()
			elif option == 3 or answer == '-backup':
				self._backup()
			elif option == 4 or answer == '-activate':
				self._activate()
			elif option == 5:
				self._Email()
			elif option == 6:
				self._user_manage('chpasswd')
			elif option == 7:
				self._user_manage('adduser')
			elif option == 8:
				self._user_manage('rmuser')
			elif option == 9:
				self._user_manage('lsuser')
			elif answer == '-start':
				System('{}sbin/nessusd start'.format(self.nessus_path),'').run()
			elif answer == '-help':
				print('Ecample usage:\n'
					  '-start    ---- Start Nessus'
					  '-setup    ---- Install script\n'
					  '-reset    ---- Reset Trial limit\n'
					  '-update   ---- Update Plugins\n'
					  '-backup   ---- Backup Nessus\n'
					  '-activate ---- Activate Code License')
				input('Press Enter To continue...')
			else:
				input('Please type number which consist in on of options.\n'
					  'Press Enter To continue...')

if __name__ == "__main__":
	nessus = Nessus()
	nessus.main()

