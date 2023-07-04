from collection_manager import CollectionManager
from program_manager import ProgramManager

class ProgramsManagement(CollectionManager):

    def return_program_by_id(self, program_id):
        """
        get program by id
        :param program_id: instance_program.id
        :return: information about program
        """
        for program in self.collection:
            if program.Program_Id == program_id:
                return f"Program id: {program.Program_Id}, Program name: {program.name}"

    def show_all_data(self):
        """
        this function return all information about programs
        :return: list of all programs
        """
        data = []
        if self.collection > 0:
            for PROGRAM in self.collection:
                data.append(f"Id: {PROGRAM.Program_Id}, Amount:{program.amount()}\n")
            return "".join(data)
        return "Don't have a programs."

if __name__ == '__main__':
    me = ProgramManager()
    program = ProgramManager()