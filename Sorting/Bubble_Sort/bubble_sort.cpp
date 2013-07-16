#include "iostream"
#define ARRAY_SIZE 100

int main(int argc, char const *argv[])
{
	int array[ARRAY_SIZE],i,j,size,temp;
	std::cout<<"\n Enter Array Size : ";
	std::cin>>size;
	std::cout<<"\n Enter Array Elements \n";
	for (i = 0; i < size; i++)
	{
		std::cin>>array[i];
	}
	std::cout<<"\n Before Sorting \n";
	for (i = 0; i < size; i++)
	{
		std::cout<<array[i];
	}
	for (i = 0; i < size; i++)
	{
		for (j = i+1; j < size; j++)
		{
			if (array[i]>array[j])
			{
				temp = array[i];
				array[i]=array[j];
				array[j]=temp;
			}
		}
	}
	std::cout<<"\n After Sorting \n";
	for (i = 0; i < size; i++)
	{
		std::cout<<array[i];
	}
	return 0;
}