#imp
p164

Special values:
associated arrays - arrays which are tagged not by numbers, but strings (probably hash) 

To know:
I have no a fkn idea how to write a summary for that...

1.  Square brackets provide us a flexible way to manipulate the arrays, because the access method is using strings, which could be modified. Just a bunch of examples:
   ```ts 
    let addr = "";
	for (let i = 0; i < 4; i++) {
		addr += customer [` address ${i}`] + "\n";
	}

	function computeValue(portfolio) {
	let total = 0.0;
	for (let stock in portfolio) {  // Для каждого пакета акций
		// в портфеле ценных бумаг:
		let shares = portfolio[stock];// получить количество акций
		let price = getQuote (stock);  // найти курс акций
		total += shares * price;  // добавить стоимость пакета
		// акций к общей стоимости
	}
	return total;  // Возвратить общую стоимость
	}
``` 
