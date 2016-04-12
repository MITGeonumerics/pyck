#include "boundingBox.h"
BoundingBox::BoundingBox(float *p1, float *p2)
{
  // Enforce lower left corner is p1 and upper right is p2
  for(int i=0; i<3; i++)
  {
    if(p1[i]>p2[i])
    {
      float tmp = p1[i];
      p1[i] = p2[i];
      p2[i] = tmp;
    }
  }

  this->p1 = p1;
  this->p2 = p2;
}

BoundingBox::~BoundingBox()
{
  delete [] p1;
  delete [] p2;
}