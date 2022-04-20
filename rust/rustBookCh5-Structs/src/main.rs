fn main() {

    struct User {
        active: bool,
        username: String,
        email: String,
        sign_in_count: u64,
    }



    let mut user1 = User {
        email: String::from("abc@123.com.ru.rs.sc.am.y.ou"), 
        username: String::from("someone"),
        active: true,
        sign_in_count: 1,
    };
    // now it can be mutated
    user1.email = String::from("abababa@example.com");
    fn build_user(email: String, username: String) -> User {
        User {
            email,
            username,
            active: true,
            sign_in_count: 1,
        }
    }

    // without Struct Update syntax - manually declaring values
    // let user2 = User {
    //     active: user1.active,
    //     username: user1.username,
    //     email: String::from("another@example.com"),
    //     sign_in_count: user1.sign_in_count,
    // };

    // With Struct update syntax - showing how fields not explicitly set should take their values from the given other instance
    // BUT! below no es bueno because the ownership of user1's "username" value was not transferred
    let user2 = User {
        email: String::from("jack@jack.com"),
        ..user1
    };
    println!("fudge {} ", user1.username)
}
