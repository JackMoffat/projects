fn main() {

let mut count = 0;
// naming a loop!
'counting_up: loop {
    println!("count={}",count);
    let mut remaining = 10;


    loop {
        println!("remaining = {}",remaining);
        if remaining == 9 {
            break;
        }
        if count == 2 {
            break 'counting_up;
        }
        remaining -= 1;
    }

    count += 1;
}
println!("end count = {}", count);

let mut counter = 0;
let result = loop {
    counter += 1;

    if counter == 10 {
        break counter * 2;
    }
}; // here semicolon at the end of the loop because it is being used in a let statement
println!("result esta {}",result);

let mut number = 3;
while number != 0 {
    println!("{}!",number);
    number -= 1;
}
println!("lift muh!");

let a = [10, 20, 30, 40, 50];
let mut index = 0;
while index < 5 {
    //ok cool! so here, index is counting and used to access sequential elements of the array a
    println!("the value is {}",a[index]); 
    index += 1;
}

for elem in a {
    println!("uhh what? {},"elem);
}

}
