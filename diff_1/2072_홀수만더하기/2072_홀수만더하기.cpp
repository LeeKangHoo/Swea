#include <iostream>

int calc(int* num)
{
	int a = 0;
	for (int i = 0; i < 10; i++)
	{
		if (num[i] % 2 == 1)
			a += num[i];
	}
	return a;
}



int main(int argc, char** argv)
{
	int count = 0;
	std::cin>>count;
	int result[count];
	int num [count][10] = {0};
	for (int i = 0; i < count;i++){
		for (int j = 0; j < 10; j++){
			std::cin>>num[i][j];
		}
		result[i] = calc(num[i]);
	}

	for (int z = 0; z < count; z++){
		std::cout<<"#"<< z+1 << " "<< result[z] << std::endl;
		}

}
