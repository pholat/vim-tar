import vim
import os
import tarfile

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

def TreeFindFile(Node root, string name):
    if root.data.getmembers() == name:
        return root
    for nodes in root.children:
        retval = TreeFindFile( nodes, name )
        if retval != None:
            return retval

root=None

def lol():
    print "LOL"

#TODO add by parent
def tarlist( string filename):
    try:
        ins=isinstance( filename, str )
        if tarfile.is_tarfile( filename if ins else filename.name ) 
            tar=tarfile.open(filename, 'r')
            if root == None:
                root = Node(tar)
            else
                root.add_child( tar )
            for a in tar.getmembers():
                vim.current.buffer.append( a.name )
        else:
            print "File: ", filename, " isn't a tar file"
    except:
        print "No such file: ", filename
    return tar

def tarbrowse(filename):
    filename = filename[1:-1]
    root.add_child( tarlist(filename) )

#TODO add enter -> enter file and add listing 
def tarenter():
    file2open=vim.current.line
    if not TreeFindFile( root, file2open ) == None:
        file2open = root.extractfile( file2open )
        tarlist(file2open)

#TODO print all again with newlisting: preorder tree walk
