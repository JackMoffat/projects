fn main() -> i32 {
    another_fungus(5);
}

fn another_fungus(x: i32) {
    println!("x is {}",x)
}

fn main() {
    print_labeled_measurements(5,'h');
}
fn print_labeled_measurements(value: i32, unit_label:char) {
    println!("REEEEEEEEEEEEEEE: {}{}",value, unit_label);

}
