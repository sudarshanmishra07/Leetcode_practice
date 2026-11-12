class Node:
  def __init__(self, data):
    self.data = data                #store node value                     
    self.next = None                #pointer to next node
def findLowestValue(head):          #assume first has minimum value
  minValue = head.data
  currentNode = head.next           #start chcking from second node
  while currentNode:                #traverse till end
    if currentNode.data < minValue: #check if current value is smalle
      minValue = currentNode.data   #update mimimum
    currentNode = currentNode.next  #move to next node
  return minValue