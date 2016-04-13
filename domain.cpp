#include <iostream>
#include <fstream>
#include <omp.h>

#include "domain.h"
#include "packer.h"
#include "boundingBox.h"
#include "shape.h"


Domain::Domain(Packer *packer)
{
  std::cout << "Initializing domain..." << std::flush;
  this->packer = packer;
  this->len = packer->len;

  dim = 3;
  if(len[2] < 2) dim = 2;

  state = new int[len[0]*len[1]*len[2]];
  pos = new double[len[0]*len[1]*len[2]*dim];

  if(dim>2)
  {
    #pragma omp parallel for schedule(static)
    for(long k=0; k<len[2]; k++){
      for(long j=0; j<len[1]; j++){
        for(long i=0; i<len[0]; i++){
          state[ID(i,j,k)] = 0;
        }
      }
    }
  } else {
    for(long k=0; k<len[2]; k++){
      #pragma omp parallel for schedule(static)
      for(long j=0; j<len[1]; j++){
        for(long i=0; i<len[0]; i++){
          state[ID(i,j,k)] = 0;
        }
      }
    }
  }

  numParticles = 0;

  std::cout << " complete" << std::endl;
}

Domain::~Domain()
{
  delete [] state;
  delete [] pos;
}

long* Domain::GetIntLength()
{
  return len;
}

int* Domain::GetState()
{
  return state;
}

double* Domain::GetPos()
{
  return pos;
}

long Domain::ID(long i, long j, long k)
{
  return i+j*len[0]+k*len[0]*len[1];
}

long Domain::DimID(long thisDim,long i, long j, long k)
{
  return thisDim+i*dim+j*dim*len[0]+k*dim*len[0]*len[1];
}

void Domain::Serialize(char *fname)
{

  std::ofstream outfile (fname, std::ios::out);
  if(outfile.is_open()) {

    std::cout << "Getting particle positions..." << std::flush;
    double *positions = GetPositions();
    std::cout << " complete" << std::endl;
    std::cout << "Getting particle states..." << std::flush;
    int *states = GetStates();
    std::cout << " complete" << std::endl;
    std::cout << "Getting number of particles..." << std::flush;
    long numParticles = GetNumParticles();
    std::cout << " complete" << std::endl;

    std::cout << "Writing to output file..." << std::flush;
    for(long i=0; i<numParticles; i++){
      outfile << positions[i*dim] << "," << positions[i*dim+1];
      if(dim==2)
      {
        outfile << "," << 0.0;
      }
      else
      {
        outfile << "," << positions[i*dim+2];
      }
      outfile << "," << states[i];
      outfile << std::endl;
    }
    outfile.close();
    std::cout << " complete" << std::endl;
  }
}

void Domain::MapShape(Shape *shape)
{
  BoundingBox *bb = shape->boundingBox;

  // Convert to domain indexes
  long *p1 = new long[3];
  long *p2 = new long[3];

  // Get the ijk extent
  // Third argument "floors" the ijk indexes (lower left corner) if true
  // "ceils" the ijk indexes (upper right corner) if false
  packer->Pos2IDX(bb->p1, p1, true);
  packer->Pos2IDX(bb->p2, p2, false);

  std::cout << "Mapping a shape..." << std::flush;

  if(dim>2)
  {
    #pragma omp parallel for schedule(static)
    for(long k=p1[2]; k<p2[2]; k++){
      double thisPos[3];
      for(long j=p1[1]; j<p2[1]; j++){
        for(long i=p1[0]; i<p2[0]; i++){
          packer->IDX2Pos(i,j,k,thisPos);
          if(shape->IsInside(thisPos)){
            state[ID(i,j,k)] = shape->state;
            pos[DimID(0,i,j,k)] = thisPos[0];
            pos[DimID(1,i,j,k)] = thisPos[1];
            if(dim>2) pos[DimID(2,i,j,k)] = thisPos[2];
          }
        }
      }
    }
  } else {
    for(long k=p1[2]; k<p2[2]; k++){
      #pragma omp parallel for schedule(static)
      for(long j=p1[1]; j<p2[1]; j++){
        double thisPos[3];
        for(long i=p1[0]; i<p2[0]; i++){
          packer->IDX2Pos(i,j,k,thisPos);
          if(shape->IsInside(thisPos)){
            state[ID(i,j,k)] = shape->state;
            pos[DimID(0,i,j,k)] = thisPos[0];
            pos[DimID(1,i,j,k)] = thisPos[1];
            if(dim>2) pos[DimID(2,i,j,k)] = thisPos[2];
          }
        }
      }
    }
  }
    std::cout << " complete" << std::endl;
}

long Domain::GetNumParticles(){
  //if(numParticles != 0) return numParticles;

  numParticles = 0;
  long totalIJK = len[0]*len[1]*len[2];
  for(long i=0;i<totalIJK;i++){
    if(state[i]!=0) numParticles++;
  }

  return numParticles;
}

double* Domain::GetPositions(){
  long numParticles = GetNumParticles();

  double *positions = new double[numParticles*dim];

  long totalIJK = len[0]*len[1]*len[2];
  long particle = 0;
  for(long i=0;i<totalIJK;i++){
    if(state[i]!=0){
      long thisIDX = i*dim;
      positions[particle] = pos[thisIDX];
      positions[particle+1] = pos[thisIDX+1];
      if(dim>2) positions[particle+2] = pos[thisIDX+2];
      particle+=dim;
    }
  }

  return positions;
}

int* Domain::GetStates(){
  long numParticles = GetNumParticles();

  int *states = new int[numParticles];

  long totalIJK = len[0]*len[1]*len[2];
  long particle = 0;
  for(long i=0;i<totalIJK;i++){
    if(state[i]!=0){
      states[particle] = state[i];
      particle++;
    }
  }

  return states;
}
