open Core;;
include Lib;;

Printf.printf "\n";;
Printf.printf "Part 1:\n";;

(* Edit this with the correct day *)
let inp = 
    [Common.read_input "./bin/11/sample.txt";
     Common.read_input "./bin/11/input.txt"]
;;

class monkey
    (s: string) (op: int -> int) (t: int -> int) =
    object(_)
        val mutable items = 
            Str.split (Str.regexp ", ") s
                |> List.map ~f:int_of_string
                |> Array.of_list
        method get_items = items
        method set_items new_items = items <- new_items
        method operation old = op old
        method throw_to worry = t worry 
    end
;;

let ops = Hashtbl.of_alist_exn (module String) 
    [("+", fun y x -> x + y); ("-", fun y x -> x - y); ("*", fun y x -> x * y)]
;;

let extract s reg =
    let _ = Str.search_forward reg s 0 in
    Str.matched_group 1 s
;;

(* Part 1 *)
List.iter ~f:(fun s ->
    (* Code goes here *)
    let l = s
        |> String.split_on_chars ~on:['\n']
        |> Array.of_list
    in
    let monkeys = 
        (Common.range 0 (Array.length l) 7)
            |> List.map ~f:(fun i ->
                let items_string = extract l.(i+1) (Str.regexp {|: \(.*\)|}) in

                let op_string = extract l.(i+2) (Str.regexp {|old \(.\)|}) in
                let op = Hashtbl.find_exn ops op_string in
                let mod_string = extract l.(i+2) (Str.regexp {|old . \(.*\)|}) in
                let modify = 
                    if String.equal mod_string "old" then
                        fun x -> op x x
                    else
                        op (int_of_string mod_string)
                in

                let test_string = extract l.(i+3) (Str.regexp {|by \(.*\)|}) in
                let throw_true_string = extract l.(i+4) (Str.regexp {|monkey \(.\)|}) in
                let throw_false_string = extract l.(i+5) (Str.regexp {|monkey \(.\)|}) in
                let throw_to x =
                    if x mod (int_of_string test_string) = 0 then
                        int_of_string throw_true_string
                    else
                        int_of_string throw_false_string
                in

                new monkey items_string modify throw_to
            )
            |> Array.of_list
    in
    let touch_counts = Array.create ~len:(Array.length monkeys) 0 in
    for _ = 1 to 20 do
        Array.iteri ~f:(fun mi m ->
            m#get_items
                |> Array.iter ~f:(fun item ->
                    let worry = (m#operation item) / 3 in
                    let next_monkey = monkeys.(m#throw_to worry) in
                    next_monkey#set_items (Array.append next_monkey#get_items [|worry|]);
                    touch_counts.(mi) <- touch_counts.(mi) + 1;
                )
            ;

            m#set_items (Array.create ~len:0 0);
        ) monkeys;
    done;

    Array.sort touch_counts ~compare:(fun x y -> y - x);
    Printf.printf "%d\n" ((touch_counts.(0)) * (touch_counts.(1)));

    (* Separate output *)
    Printf.printf "-------\n";
) inp;;

(* modulus by a consistent factor to avoid overflow in p2 *) 
let modulus = 23 * 17 * 13 * 11 * 5 * 2 * 7 * 19 * 3;;
Printf.printf "\nPart 2:\n";;
(* Part 2 *)
List.iter ~f:(fun s ->
    (* Code goes here *)
    let l = s
        |> String.split_on_chars ~on:['\n']
        |> Array.of_list
    in
    let monkeys = 
        (Common.range 0 (Array.length l) 7)
            |> List.map ~f:(fun i ->
                let items_string = extract l.(i+1) (Str.regexp {|: \(.*\)|}) in

                let op_string = extract l.(i+2) (Str.regexp {|old \(.\)|}) in
                let op = Hashtbl.find_exn ops op_string in
                let mod_string = extract l.(i+2) (Str.regexp {|old . \(.*\)|}) in
                let modify = 
                    if String.equal mod_string "old" then
                        fun x -> op x x
                    else
                        op (int_of_string mod_string)
                in

                let test_string = extract l.(i+3) (Str.regexp {|by \(.*\)|}) in
                let throw_true_string = extract l.(i+4) (Str.regexp {|monkey \(.\)|}) in
                let throw_false_string = extract l.(i+5) (Str.regexp {|monkey \(.\)|}) in
                let throw_to x =
                    if x mod (int_of_string test_string) = 0 then
                        int_of_string throw_true_string
                    else
                        int_of_string throw_false_string
                in

                new monkey items_string modify throw_to
            )
            |> Array.of_list
    in
    let touch_counts = Array.create ~len:(Array.length monkeys) 0 in
    for _ = 1 to 10000 do
        Array.iteri ~f:(fun mi m ->
            m#get_items
                |> Array.iter ~f:(fun item ->
                    let worry = (m#operation item) mod modulus in
                    let next_monkey = monkeys.(m#throw_to worry) in
                    next_monkey#set_items (Array.append next_monkey#get_items [|worry|]);
                    touch_counts.(mi) <- touch_counts.(mi) + 1;
                )
            ;

            m#set_items (Array.create ~len:0 0);
        ) monkeys;
    done;
    
    Array.sort touch_counts ~compare:(fun x y -> y - x);
    Printf.printf "%d\n" ((touch_counts.(0)) * (touch_counts.(1)));

    (* Separate output *)
    Printf.printf "-------\n";
) inp;;
