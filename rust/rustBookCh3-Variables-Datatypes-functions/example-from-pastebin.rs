/**
 * Tasks:
 * - Convert Fahrenheit and Celsius
 * - Generate the nth Fibonacci number
 * - Print lyrics of the Twelve Days of Christmas
 */

use std::io;
use std::str::FromStr;

const F2C_OFFSET: f32 = 32.;
const F2C_SCALE: f32 = 5./9.;

fn fahrenheit_to_celsius(fahrenheit: f32) -> f32 {
	(fahrenheit - F2C_OFFSET) * F2C_SCALE
}

fn celsius_to_fahrenheit(celsius: f32) -> f32 {
	(celsius / F2C_SCALE) + F2C_OFFSET
}

fn temp_converter(){
	let converter : fn (f32) -> f32 = loop {
		let prompt = "Temperature converter.\n\
			1) Fahrenheit to Celsius\n\
			2) Celsius to Fahrenheit";
		let choice : i32 = ask_number(prompt);
		match choice {
			1 => break fahrenheit_to_celsius,
			2 => break celsius_to_fahrenheit,
			_ => {println!("Wrong input"); continue;}
		};
	};
	let prompt = "Enter the temperature";
	let temperature : f32 = ask_number(prompt);
	let result = converter(temperature);
	println!("Result: {}", result);
}

fn fibo(mut input: i32) -> i128 {
	assert!(input >= 0);
	match input {
		0 => 1,
		1 => 1,
		_ => {
			let mut pred = 1;
			let mut cur = 1;
			let mut tmp;
			while input >= 2 {
				tmp = pred;
				pred = cur;
				cur = tmp + pred;
				input -= 1;
			};
			cur
		}
	}
}

fn fibonacci(){
	let prompt = "Fibonacci computer\n\
		Enter a number";
	let input = loop {
		let choice : i32 = ask_number(prompt);
		if choice < 0 {
			println!("Wrong input, should be positive");
			continue
		} else { break choice }
	};
	let result = fibo(input);
	println!("fibo({}) = {}", input, result)
}

const ORDINALS: [&str; 12] = ["first", "second", "third", "fourth", "fifth",
	"sixth", "seventh", "eight", "ninth", "tenth", "eleventh", "twelfth"];
fn ordinal(i: i32) -> &'static str {
	assert!(i >= 0 && i < 12);
	ORDINALS[i as usize]
}

fn lyrics(){
	let presents = ["a partridge in a pear tree", "two turtle doves",
		"three French hens", "four calling birds", "five gold rings",
		"six geese a laying", "seven swans a swimming", "eight maids a milking",
		"nine ladies dancing", "ten lords a leaping", "eleven pipers piping",
		"12 drummers drumming"];
	for i in 0..12 {
		println!("On the {} day of Christmas", ordinal(i));
		println!("My true love gave to me");
		for j in (0..i+1).rev() {
			let prefix = if j < i { "and " } else {""};
			println!("{}", format!("{}{}", prefix, presents[j as usize]));
		}
		println!("");
	}
}

fn ask_number<T: FromStr>(question: &str) -> T {
	println!("---------------------------------");
	println!("{}", question);
	let mut choice = String::new();
	loop {
		io::stdin().read_line(&mut choice)
			.expect("Failed to read input");
		let choice : T = match choice.trim().parse() {
			Ok(num) => num,
			Err(_) => continue
		};
		break choice
	}
}

fn main() {
	loop {
		let prompt = "What would you like to do?\n\
			1) Convert temperature\n\
			2) Generate Fibonacci number\n\
			3) Print the lyrics of a nice song\n\
			4) Quit";
		let choice : i32 = ask_number(prompt);
		match choice {
			1 => temp_converter(),
			2 => fibonacci(),
			3 => lyrics(),
			4 => break,
			_ => println!("Wrong input")
		};
	}
}
