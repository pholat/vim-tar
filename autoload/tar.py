import vim
import os
import tarfile

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

def TreeFindFile( root, name ):
    print "Looking in: ",root.data.name, " : ", name
    for a in root.data.getmembers():
        print a.name
        if a.name == name:
            return root
    for nodes in root.children:
        retval = TreeFindFile( nodes, name )
        if retval != None:
            return retval

def lol():
    print "LOL"

class Tree():
    root=None

#TODO add by parent
def tarlist( filename ):
#    try:
    ins=isinstance( filename, str )
    if tarfile.is_tarfile( filename if ins else filename.name ):
        tar=tarfile.open(filename, 'r')
        if Tree.root == None:
            Tree.root = Node(tar)
        else:
            Tree.root.add_child( tar )
        for a in tar.getmembers():
            vim.current.buffer.append( a.name )
        return tar
    else:
        print "File: ", filename, " isn't a tar file"
#    except:
#        print "No such file: ", filename, a.str()

def tarbrowse(filename):
    filename = filename[1:-1]
    tmpvar=tarlist(filename)

#TODO add enter -> enter file and add listing 
def tarenter():
    file2open=vim.current.line
    if not TreeFindFile( Tree.root, file2open ) == None:
        file2open = Tree.root.data.extractfile( file2open )
        tarlist(file2open)

#TODO print all again with newlisting: preorder tree walk
