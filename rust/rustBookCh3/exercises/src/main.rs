fn main() {
    for idx in 0..11 {
        generate_lyrics(idx);
    };
}

fn generate_lyrics(n: i32) {
    let numbers_brutally_implemented = [
        "a",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
    ];
    let day_names_brutally_implemented: [&str; 12] = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eight",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth",
    ];
    let day_gift = [
        "partridge in a pear tree",
        "turtle doves",
        "french hens",
        "calling birds",
        "golden rings",
        "geese a-laying",
        "swans a-swimming",
        "maids a-milking",
        "ladies dancing",
        "lords a-leaping",
        "pipers piping",
        "drummers drumming"
    ];

    // let mut index = 0;
    use std::convert::TryInto;
    for idx in 0..n {
        // why doesn't this variable need to be mutable?
        let index:usize = idx.try_into().unwrap();
        let day_name = day_names_brutally_implemented[index];
        println!("on the {} day of christmas my true love gave to me",day_name);
        for interior_idx in (0..idx+1).rev() {
            let interior_index:usize = interior_idx.try_into().unwrap();
            if index > 0 && interior_index == 0 {
                println!("and {} {}",numbers_brutally_implemented[interior_index],day_gift[interior_index]);
            } else {
                println!("{} {}",numbers_brutally_implemented[interior_index],day_gift[interior_index]);
            };
           }
        };
    }
