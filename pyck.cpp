#include <iostream>

#include "pyck.h"
#include "packers/fccPacker.h"
#include "packers/hcpPacker.h"
#include "packers/bccPacker.h"
#include "packers/cubicPacker.h"
#include "domain.h"
#include "shapes/cuboid.h"
#include "shapes/sphere.h"
#include "shapes/cylinder.h"

int main()
{
  double size[3];
  size[0] = 1; size[1] = 1; size[2] = 1.0;

  double h = 0.0005;

  // Sphere properties
  double r = 0.2;
  double c[3];
  c[0] = 0.5; c[1] = 0.5; c[2] = 0.0;


  // Cylinder properties
  double l[3];
  l[0] = 0.0; l[1] = 0.0; l[2] = 0.1;
  double rc = 0.1;
  double cc[3];
  cc[0] = 0.5; cc[1] = 0.5; cc[2] = 0.0;
  /*  double l2[3];
  l2[0] = 0.0; l2[1] = -0.2; l2[2] = 0.0;*/


  // Cuboid properties
  double p1[3], p2[3], p3[3], p4[3];
  p1[0] = 0.3; p1[1] = 0.1; p1[2] = 0.2;
  p2[0] = 0.7; p2[1] = 0.9; p2[2] = 0.8;
  p3[0] = 0.4; p3[1] = 0.4; p4[2] = 0.2;
  p4[0] = 0.6; p4[1] = 0.6; p3[2] = 0.8;

  // Create a new packer
  CubicPacker *packer = new CubicPacker(size,h);

  // Create a new domain
  Domain *domain = new Domain(packer);

  // Create and pack a shape
  Cuboid *box = new Cuboid(1,p1,p2);
  Sphere *sphere = new Sphere(2,c,r);
  Cylinder *cylinder = new Cylinder(3,cc,rc,l);
  // Cylinder *box2 = new Cylinder(2,c,r,l2);
  // Cuboid *clearbox = new Cuboid(2,p3,p4);
  domain->MapShape(box);
  //domain->MapShape(sphere);
  //domain->MapShape(cylinder);

  // Count particles
  long numParticles = domain->GetNumParticles();

  std::cout << numParticles << " particles packed" << std::endl;

  // Write domain to a CSV
  std::string filename = "bcctest.csv";
  //domain->Serialize((char*)filename.c_str());

  std::cout << "Packing Complete\n";
  std::cout << "File " << filename << " generated" << std::endl;
  delete box;
  delete sphere;
  delete cylinder;
  delete packer;
  delete domain;
}
