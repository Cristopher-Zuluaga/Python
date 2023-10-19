#include<iostream>
using namespace std;

class circulo
{
      private;
              double radio;
      public;
             double obtengaRadio() const;
             double obtengaArea() const;
             double obtengaPerimetro() const;
             void AsigneRadio(double r);
}

double Circulo::obtengaRadio()
{
       return radio;
}
double Circulo::obtengaArea()
{
       const double PI=3.141593;
       double area= Pi*radio*radio;
       return area;
}
double Circulo::obtenga Perimetro()
{
       const double PI = 3.141593;
       double perimetro = 2*PI*radio;
       return perimetro;
}
void AsigmeRadio(double r)
{
     radio=r;
}
int main()
{
    Circulo circulo1;
    circulo1.asigneRadio(5.0);
    cout<<"Circulo 1: "<<endl;
    cout<<"Radio: "<< circulo1.obtengaRadio() <<endl;
    cout<<"Area: "<< circulo1.obtengaArea() <<endl;
    cout<<"Perimetro: "<< circulo1.obtengaPerimetro() <<endl;    
    return 0;
}