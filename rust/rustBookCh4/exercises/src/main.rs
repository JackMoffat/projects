use std::io;

fn main() {

    get_input();
    // let (user_temp, user_unit) = get_input();

}

fn get_input() -> String {
    let mut user_input = String::new();
    println!("please enter the temperature and single-letter abbreviation of the unit to convert, to at least one decimal point in accuracy, separated by a space (eg. 203.0 c or 203.1 f or 203.868 C or 203.4 F)");
    io::stdin().read_line(&mut user_input).expect("expect....?");
    // split the string apart

    let bytes = user_input.as_bytes();
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            // return (&user_input[0..i],&user_input[i..]);
            let tup = (&user_input[0..i],&user_input[i..]);
            tup
        } else {
            user_input;
        }
    }
}
