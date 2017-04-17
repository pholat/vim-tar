import vim
import os
import tarfile

class Node(object):
    def __init__(self, data ):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

def lol():
    print "LOL"

class Tree():
    root=None
    tmpdepth=0

    """ Returns first (Node,depth) which has element with <name> in <data> 
        returns None if there is no such element
    """
    def FindFile( self, root, name, depth=0 ):
        print "Looking in: ",root.data.name, " : ", name, "depth: ", depth
        for a in root.data.getmembers():
            if a.name == name:
                return (root, depth)
        for nodes in root.children:
            retval = FindFile( nodes, name, depth+1 )
            if retval != None:
                return retval

# TODO subtract prefix in tarenter in name
def tarlist( filename, depth ):
    tar=tarfile.open(filename, 'r')
    prefix=''
    for a in range( depth ):
        prefix+='-'
    prefix +='> '
    for a in tar.getmembers():
        #TODO CD THIS PREFIX
        vim.current.buffer.append( prefix + a.name )
    return tar

def prefix_subrtact():
    None

""" Opens tarfile passed as argument and adds it as a root """
def tarbrowse(filename):
    filename = filename[1:-1]
    tar = tarfile.open( filename )
    Tree.root = Node(tar)
    tarenter(filename)

def tarenter(file2open):
    file2open = prefix_subtract(file2open)
    fileNode = Tree.FindFile( Tree.root, file2open )
    if not fileNode == None:
        # TODO extract as temporary/to ram somehow
        file2open.data.extract( file2open )
        if tarfile.is_tarfile( file2open ):
            tar=tarfile.open( file2open )
            # THIS IS NOT C++ we do not work on pointer but on copy -> do something with that...
            fileNode[0].add_child( Node( tar ) )
            tarlist( file2open, fileNode[1] )
        else:
            # TODO in new buffer named after that file ... 
            vim.current.buffer.append( File(file2open).read() )
    else:
        print "No such file ... something went terribly wrong"

def TarEnter():
    file2open=vim.current.line
    tarenter(file2open)
