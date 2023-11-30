import numpy as np

def makeArray():
    '''Creates a NumPy ndarray identical to one written in config.txt'''
    # Open text file for reading user input. Input is seperated by whitespace " ".
    with open('config.txt') as f:
        lines = f.readlines()
        f.close()

    for i in range(lines.__len__()):
        if '\n' in lines[i]: 
            lines[i].replace('\n', '') # Remove all \n characters 
        lines[i] = lines[i].split() # Split numbers at whitespace seperator.
    
    setToRemove = []
    for i in lines:
        if i == [] or i[0] == '#':
            setToRemove.append(i)

    for i in setToRemove:
        lines.remove(i)

    M = np.ndarray(shape=(lines.__len__(), lines[0].__len__()), dtype="float") # Create ndarray from dimensions of txt document.

    for i in range(lines.__len__()):
        for e in range(lines[i].__len__()):
            if lines[i][e] == ' ' or lines[i][e] == '':
                continue
            M[i][e] = int(lines[i][e])
    
    return M

def isSquare(M):
    '''Returns true if the target matrix is square.'''
    return M.shape[0] == M.shape[1]

def matriceDet(M):
    '''Takes an NumPy array or ndarray of integers or floats of size 1x1, 2x2 or 3x3 and returns its determinant as a float.'''
    if not isSquare(M):
        print("ERROR: Invalid input. Input matrix M must be square.")
        return
    
    

def multiply(A, B):
    if (A.shape[1] != B.shape[0]):
        print(f"ERROR: Invalid input. Input matrices A and B must match. {A.shape[1]} must equal {B.shape[9]}.")
        return
    M = np.ndarray(A.shape[0], B.shape[1])
    M = A * B
    #WIP

if __name__ == "__main__":
    M = makeArray()
    print(M)
    #matriceDet(M)