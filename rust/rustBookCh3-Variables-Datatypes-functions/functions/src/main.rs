fn main() {
    another_fungus(5);
}

fn another_fungus(x: i32) {
    println!("x is {}",x)
}

fn main() {
    print_labeled_measurements(5,'h');
}
fn print_labeled_measurements(value: i32, unit_label:char) {
    println!("measurements! : {}{}",value, unit_label);

}

let y = {
    let x = 3; // statement!!!
    x + 1 // expression 
};

fn five() -> i32{
    5
}

fn main() {
    let x = five();
    println!("x is {}",x); // see, technically a statement but since it is a macro....something something
}
