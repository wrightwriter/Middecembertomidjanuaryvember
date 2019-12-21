
rx = 1000
ry = 1000

pi = acos(-1)
tau = 2*pi


def makeShape(numVertices, radius, position):
    shape = []
    for idx in range(0, numVertices):
        i = tau*idx/numVertices
        vertex = PVector(sin(i), cos(i)) * radius 
        vertex = vertex - position
        shape.append( vertex )
    return shape

def drawLinePVector(a, b):
    line(a.x, a.y, b.x, b.y)

def drawShape(inShape):
    numVerts = len(inShape)
    for idxVert in range(0,numVerts):
         drawLinePVector( inShape[idxVert], inShape[(idxVert + 1)%numVerts] )

def drawShapes(shapes):
    numShapes = len(shapes)
    for idxShape in range(0,numShapes):
         drawShape(shapes[idxShape])

def makeAuraOfShapes(numOuterShapes, innerRadius, outerRadius, numReps, globalOffset):
    shapes = []
    for idx in range(0, numOuterShapes):
        i = tau*idx/numOuterShapes
        offset = PVector(sin(i), cos(i))*outerRadius - PVector(ry/2,ry/2) - globalOffset
        currShape = makeShape(numReps, innerRadius, offset)
        shapes.append( currShape )
        #drawShape(currShape)    
    return shapes

def drawCirclesAtVerticesOfShape(inShape, radius):
    for vert in inShape:
        circle(vert.x, vert.y, radius)
        
def drawCircleAtVerticesOfShapeAtIdx(inShape, radius,idx):
        circle(inShape[idx].x, inShape[idx].y, radius)

   
def lerpPs(shapeArray, i, rangeI):
    lenShape = len(shapeArray)
    idx = floor(lenShape * i/rangeI)
    idxFrac = (lenShape * i/rangeI)%1
    return shapeArray[idx].lerp(shapeArray[(idx + 1)%lenShape], idxFrac)


def draw():
    filter(THRESHOLD);
        

def setup():
    size(rx, ry)
    background(0)
    stroke(255)
    noFill()
    strokeWeight(0.5)
    
    shapeA = []
    shapeB = []
    shapeC = []
    
    shapesOuter = []  
    
    beginShape()
    # make outer part

    innerRadius = 0.1*rx
    outerRadius = innerRadius
    offset      = PVector(0,0)
    coolShapesA = makeAuraOfShapes(6, innerRadius, outerRadius, 4, offset)

    innerRadius *= 2.0
    offset      = PVector(0,-outerRadius*4)
    outerRadius = innerRadius*1.47
    coolShapesD = makeAuraOfShapes(6, innerRadius, outerRadius, 4, offset)
    offset.x = -offset.x
    offset.y = -offset.y 
    coolShapesE = makeAuraOfShapes(6, innerRadius, outerRadius, 4, offset)

    offset      = PVector(0,0)
    innerRadius = 0.3*rx
    coolShapesB = makeAuraOfShapes(4, innerRadius, outerRadius, 6, offset)

    offset      = PVector(0,0.4*rx)
    innerRadius = 0.3*rx
    TriA = makeAuraOfShapes(1, innerRadius, outerRadius, 3, offset)
    
    innerRadius = 0.22*rx
    offset = offset + PVector(0,0.27*rx)
    TriB = makeAuraOfShapes(1, innerRadius, outerRadius, 3, offset)

    offset      = PVector(0,0.15*rx)
    innerRadius = 0.6*rx
    coolShapesC = makeAuraOfShapes(1, innerRadius, outerRadius, 4, offset)
    

    drawShapes(coolShapesA)
    #drawShapes(coolShapesB)
    drawShapes(coolShapesC)
    drawShapes(coolShapesE)
    drawShapes(coolShapesD)
    #drawShapes(TriA)
    drawShapes(TriB)




    for sh in coolShapesC:
        drawCircleAtVerticesOfShapeAtIdx(sh, 0.1*rx, 0)
    

    #for idx in range(0, numOuterShapes):

    endShape()
