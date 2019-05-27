//Список студентов
var groupmates = [
    {
        "name": "Костя",
        "group": "17_02",
        "age": 19,
        "marks": [5, 3, 3, 5, 4]
    },
    {
        "name": "Василий",
        "group": "17_03",
        "age": 21,
        "marks": [4, 2, 2, 4, 3]
    },
    {
        "name": "Георгий",
        "group": "17_02",
        "age": 18,
        "marks": [2, 5, 5, 3, 5]
    },
    {
        "name": "Валентина",
        "group": "17_01",
        "age": 18,
        "marks": [5, 5, 5, 4, 5]
    },
	{
        "name": "Мария",
        "group": "17_02",
        "age": 19,
        "marks": [5, 5, 5, 3, 3]
    },
];
console.log(groupmates);

var rpad = function(str, length) {
    str = str.toString(); // преобразование в строку
    while (str.length < length)
        str = str + ' '; // добавление пробела в конец строки
    return str; // когда все пробелы добавлены, возвратить строку
};
var printStudents = function(students){
    console.log(
        rpad("Имя студента", 15),
        rpad("Группа", 8),
        rpad("Возраст", 8),
        rpad("Оценки", 20)
    );
    // был выведен заголовок таблицы
    for (var i = 0; i<=students.length-1; i++){
        // в цикле выводится каждый экземпляр студента
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['age'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n'); // добавляется пустая строка в конце вывода
};
printStudents(groupmates);

//Переменная с номером сортируемой группы
var group_num="17_02";
console.log("Номер группы для сортировки: "+group_num);
console.log('\n');

//Функция вывода студентов нужной группы
var sort_stud=function(students)
{
	console.log(
        rpad("Имя студента", 15),
        rpad("Группа", 8),
        rpad("Возраст", 8),
        rpad("Оценки", 20)
    );
	for (var i=0;i<students.length;i++)
	{
		if (students[i]['group']==group_num)
		{
			console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['age'], 8),
            rpad(students[i]['marks'], 20)
        );
		}
	}
}
sort_stud(groupmates);