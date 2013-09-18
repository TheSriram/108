package sorting;

import java.util.ArrayList;

public class QuickSort {

	//ArrayList<Integer> array = new ArrayList<Integer>();
	Integer[] arrayToBeSorted = new Integer[10];
	
	public QuickSort(Integer[] arrayToBeSorted){
		//this.array = array;
		this.arrayToBeSorted = arrayToBeSorted;
	}
	
	public void swap(int a, int b){
		int temp = arrayToBeSorted[a];
		arrayToBeSorted[a] = arrayToBeSorted[b];
		arrayToBeSorted[b] = temp;	
	}
	
	public int partition(int left, int right, int pivotIndex){
		int pivot = arrayToBeSorted[pivotIndex];
		swap(pivotIndex, right);
		int storeIndex = left;
		for(int i=left; i<arrayToBeSorted.length -1; i++){
			if(arrayToBeSorted[i] < arrayToBeSorted[right]){
				swap(i, storeIndex);
				storeIndex++ ;
			}
		}
		swap(storeIndex, right);
		return storeIndex;
	}
	
	public Integer[] recursiveQS(int left,int right, QuickSort qs){
		
		if(left < right){
			int pivotIndex = (left+right)/2;
			int partitionIndex = qs.partition(left, right, pivotIndex);
			System.out.println("Partition Index : " + partitionIndex);
			qs.recursiveQS(left, partitionIndex-1, qs);
			qs.recursiveQS(partitionIndex+1, right, qs);
		}
		return arrayToBeSorted;
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Integer[] arrayToBeSorted = {9,8,7,6,5,4,3,2,1,0};
		QuickSort qs = new QuickSort(arrayToBeSorted);
		//System.out.println(qs.partition(0, arrayToBeSorted.length-1, 9));
		Integer[] sortedArray = qs.recursiveQS(0, arrayToBeSorted.length-1, qs);
		for(int i =0; i<arrayToBeSorted.length; i++){
			System.out.print(" "+sortedArray[i]+" ");
		}
	}

}
