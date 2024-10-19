import csv
import os


# Technically dictionary in memory is also database and i went a bit further
class DataController:
    def __init__(self, file, fields):
        self.file = file
        self.fields = fields
        self.key = fields[0]

        if not os.path.exists(file):
            with open(file, 'w'):
                pass
    
    def read(self):
        file = open(self.file, "r")
        return csv.DictReader(file, fieldnames=self.fields), file.close
    
    def readAll(self):
        with open(self.file, "r") as file:
            return list(csv.DictReader(file.readlines(), fieldnames=self.fields))

    
    def find(self, value):
        (entries, close) = self.read()
        for entry in entries:
            if entry[self.key] == value:
                close()
                return entry
        close()
        return None

    def add(self, *args):
        if self.find(args[0]):
            return False
        
        with open(self.file, "a") as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writerow(dict(zip(self.fields, args)))
        return True
    
    def remove(self, value):
        find = self.find(value)
        if not find:
            return None
        
        entries = self.readAll()
        with open(self.file, "w") as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            for entry in entries:
                if entry[self.key] == value:
                    continue
                writer.writerow(entry)
        return find
