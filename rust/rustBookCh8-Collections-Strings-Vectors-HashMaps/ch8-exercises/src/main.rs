// in rust this would be an array
fn main() {
    list = [20, 6, 2, 1, 16, 14, 2, 2, 19, 5, 9, 4, 1, 10, 3, 1, 12, 2, 7, 10, 17, 14, 3, 5, 10, 7, 1, 8, 7, 16, 5, 0, 12, 3, 0, 18, 6, 6, 8, 3];

    let v: Vec<i32> = Vec::new();

    for elem in list {
        v.push(elem);
    }

    println!("{:?}",v);
}
