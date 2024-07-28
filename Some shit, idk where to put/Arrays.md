
#loops  Here’s a simple solution to your problem using these concepts:

```typescript 
function transformArray(arr, fn) {
    let result = [];
    for(let i = 0; i < arr.length; i++) {
        result.push(fn(arr[i], i));
    }
    return result;
}
```

In this code, `transformArray` is a function that takes an array `arr` and a function `fn` as arguments. It creates a new array `result`, and then it uses a `for` loop to iterate over `arr`. For each element in `arr`, it calls `fn` with the element and its index as arguments, and then it adds the result to `result`. Finally, it returns `result`. This achieves the same result as `Array.map`, but without using `Array.map`.

```ts
interface Array<Type> {

/**

* Получает или устанавливает длину массива

*/

length: number

/**

* Удаляет последний элемент массива и возвращает его

*/

pop(): Type | undefined

/**

* Добавляет новые элементы в конец массива и возвращает новую длину массива

*/

push(...items: Type[]): number

// ...

}
```


  #algs
  Добре, ось покрокова інструкція для написання бінарного пошуку в JavaScript:

```javascript
function binarySearch(array, target) {
    let left = 0;
    let right = array.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);

        if (array[mid] === target) {
            return mid;
        }
        if (array[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}
```

1. **Створюємо функцію `binarySearch` з двома параметрами: `array` і `target`.** `array` - це масив, в якому ми шукаємо, а `target` - це елемент, який ми хочемо знайти.
    
2. **Визначаємо дві змінні `left` і `right` для відстеження частини масиву, в якій ми шукаємо.** `left` вказує на початок масиву, а `right` - на кінець. Ми використовуємо `array.length - 1`, а не просто `array.length`, тому що індексація масиву в JavaScript починається з 0.
    
3. **Створюємо цикл `while`, який продовжується, поки `left` не стане більшим за `right`.** Це означає, що ми продовжуємо пошук, поки не переглянемо весь масив.
    
4. **В середині циклу ми визначаємо `mid` як середину між `left` і `right`.** Ми використовуємо `Math.floor` для округлення до найближчого цілого числа, тому що індекси масиву повинні бути цілими числами.
    
5. **Потім ми порівнюємо `target` з елементом в `array[mid]`.** Якщо вони рівні, ми повертаємо `mid`, тому що ми знайшли елемент.
    
6. **Якщо `target` більше, ніж `array[mid]`, ми змінюємо `left` на `mid + 1`.** Це означає, що ми відкидаємо ліву половину масиву і продовжуємо пошук в правій половині.
    
7. **Якщо `target` менше, ніж `array[mid]`, ми змінюємо `right` на `mid - 1`.** Це означає, що ми відкидаємо праву половину масиву і продовжуємо пошук в лівій половині.
    
8. **Якщо ми вийшли з циклу і не знайшли елемент, ми повертаємо `-1`.** Це стандартний спосіб показати, що елемент не знайдено в масиві.
    

Цей алгоритм працює, тому що масив впорядкований. Якщо масив не впорядкований, бінарний пошук не буде працювати. Бінарний пошук ефективний, тому що він розбиває масив навпіл з кожним кроком, зменшуючи кількість даних, які потрібно переглянути, вдвічі. Це робить бінарний пошук набагато швидшим, ніж лінійний пошук для великих масивів.

напиши покрокову інструкцію з уточненням"чому ми робимо таке, а не інакше, i як працює той чи інший інструмент і синтаксис, який ти використав(наприклад чому ти написав array.length а не просто array)" відносно кожного кроку. Напиши інструкцію по такому шаблону для написання бінарного пошуку в JS