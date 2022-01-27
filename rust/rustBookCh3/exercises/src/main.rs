use std::io;

fn main() {

    convert_temperature();

}

fn convert_temperature(unit: String) {
    // current status of this bad boy is that it'll work (ish) if given correct unit at the outset, but will
    // not if given teh correct unit after an incorrect guess.
    // this is somehow due to stdin and &mut saving the info of what user_unit is in the loop somehow
    // will retunr to 
    const RATIO_DEG_F_PER_C: f32 = 2.12;
    // displayed instructions
    loop {
        // create variable to hold user input
        let mut user_temperature = String::new();
        // get user input and ...mutate or shadow it here when it is returned? or, does neither happen because it was made with just String::new(?)
        println!("temperature?");
        io::stdin().read_line(&mut user_temperature).expect("expect....?");

        // from looking at guessing_game
        // weird, adding the trim() was all it took to make this thing work
        // it makes it look like an int is returned, but the math shows that it is getting it as an f32
        let user_temperature: f32 = match user_temperature.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
        let user_converted_temperature: f32 = if user_unit == "C" { user_temperature * RATIO_DEG_F_PER_C } else {user_temperature / RATIO_DEG_F_PER_C};
        // i got the {:.3 syntax by searching google, we encountered it in the rust by exampe}
        println!("input is currently {}\nconverted temperature:{:.3}",user_temperature,user_converted_temperature);
        break;
    };
}


fn get_unit() {
    let mut user_unit = String::new();
    let user_unit = loop {
        println!("Celsius(C) or fahrenheit?(F)");
        io::stdin().read_line(&mut user_unit).expect("expect....?");
        println!("user unit {}",user_unit);
        let user_unit_internal = user_unit.trim();
        if user_unit_internal == "C" || user_unit_internal == "F" {
            println!("user unit internal success is {}", user_unit_internal);
            break user_unit_internal; }
        else {
            println!("try again ya dingus");
            continue;
        };

    };
}
