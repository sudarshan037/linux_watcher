import getpass
import pathlib
from crontab import CronTab
from pytz import timezone
from datetime import datetime


class CronManager:
    '''
    Used for listing, creating, deleting crons.
    Instructions:
        __init__(): place this file in root folder of your project
        show_cron(): returns details of named cron
        show_crons(): returns list of all crons
        generate_cron(): takes (python, file, output(optional)) paths as input and returns cron command
        add_cron(): takes the generated cron command and adds it to crontab
        delete_cron() delete the named cron
    '''
    def __init__(self):
        self.user_info = "XDG_RUNTIME_DIR=/run/user/$(id -u)"
        self.cwd = str(pathlib.Path(__file__).parent.absolute()) + '/'
        self.python_path, self.file_path, self.output_path = None, None, None
        self.crons = CronTab(user=getpass.getuser())

    def show_cron(self, comment):
        for cron in self.crons:
            if cron.comment == comment:
                return cron

    def show_crons(self):
        return self.crons

    def __set_python_path(self, python):
        self.python_path = python

    def __set_file_path(self, file):
        self.file_path = self.cwd + file

    def __set_output_path(self, output):
        self.output_path = self.cwd + output

    def generate_cron(self, **kwargs):
        if kwargs['python']:
            self.__set_python_path(kwargs['python'])
        if kwargs['file']:
            self.__set_file_path(kwargs['file'])

        my_command = " ".join((
            self.user_info,
            self.python_path,
            self.file_path))

        if kwargs['output']:
            self.__set_output_path(kwargs['output'])
            my_command += ' >> ' + self.output_path

        return my_command

    def add_cron(self, command, comment):
        job = self.crons.new(command=command, comment=comment)
        job.minute.every(1)
        self.crons.write()
        print("Cron Added:\n", self.crons[-1])

    def delete_cron(self, comment):
        for cron in self.crons:
            if cron.comment == comment:
                self.crons.remove(cron)
                self.crons.write()


if __name__ == "__main__":
    cron_manager = CronManager()

    # create cron
    cron_command = cron_manager.generate_cron(
        python='/home/pc/Projects/linux_watcher/venv/bin/python3',
        file='main.py',
        output='out.txt')
    cron_manager.add_cron(cron_command, comment='linux_watcher')

    # show cron
    # cron_manager.show_cron('name')

    # delete cron
    # cron_manager.delete_cron('name')