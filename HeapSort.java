public class HeapSort {
    public static void heapSort(int[] arr) {
        int n = arr.length;

        
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        // извлекаем элементы из кучи и снова строим кучу
        for (int i = n - 1; i > 0; i--) {
            
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            heapify(arr, i, 0);
        }
    }

    public static void heapify(int[] arr, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && arr[left] > arr[largest]) {
            largest = left;
        }

        if (right < n && arr[right] > arr[largest]) {
            largest = right;
        }

        if (largest != i) {
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;

            heapify(arr, n, largest);
        }
    }

    public static void main(String[] args) {
        int n = 10;
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = (int) (Math.random() * 100);
        }

        heapSort(arr);

        System.out.println("Отсортированный массив:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}