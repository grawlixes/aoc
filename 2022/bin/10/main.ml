open Core;;
include Lib;;

Printf.printf "\n";;
Printf.printf "Part 1:\n";;

(* Edit this with the correct day *)
let inp = 
    [Common.read_input "./bin/10/sample.txt";
     Common.read_input "./bin/10/input.txt"]
;;

let get_val s = 
    let l = String.length s in
    int_of_string (String.sub s ~pos:5 ~len:(l-5))
;;

(* Part 1 *)
List.iteri ~f:(fun _ s ->
    (* Code goes here *)
    let x = ref 1 in
    let cycle = ref 0 in
    let can_perform = ref false in
    let checks = [20; 60; 100; 140; 180; 220] in
    s
        |> String.split_on_chars ~on:['\n']
        |> List.filter ~f:(fun s -> String.length s > 0)
        |> fun l -> 
            let rec sol = function
                | [] -> 0
                | inst :: t as lst ->
                    cycle := !cycle + 1;
                    
                    let add =
                        if List.mem checks !cycle ~equal:Int.equal then
                            (!cycle * !x)
                        else
                            0
                    in
                    if not (String.equal inst "noop") then (
                        if !can_perform then (
                            can_perform := false;
                            x := !x + (get_val inst);
                            add + (sol t)
                        ) else ( 
                            can_perform := true;
                            add + (sol lst)
                        )
                    ) else
                        add + (sol t)
            in
            sol l
        |> Printf.printf "%d\n"
    ;

    (* Separate output *)
    Printf.printf "-------\n";
) inp;;

Printf.printf "\nPart 2:\n";;
(* Part 2 *)
List.iteri ~f:(fun _ s ->
    (* Code goes here *)
    let left = ref 0 in
    let cycle = ref 0 in
    let can_perform = ref false in
    let img = Array.create ~len:(40*6) 'x' in
    s
        |> String.split_on_chars ~on:['\n']
        |> List.filter ~f:(fun s -> String.length s > 0)
        |> fun l -> 
            let rec sol = function
                | [] -> ()
                | inst :: t as lst ->
                    let left_actual = !left mod 40 in
                    let cycle_actual = !cycle mod 40 in
                    if (left_actual <= cycle_actual) && (cycle_actual <= left_actual+2) then (
                        img.(!cycle) <- '#';
                    ) else (
                        img.(!cycle) <- '.';
                    );

                    cycle := !cycle + 1;
                    
                    if not (String.equal inst "noop") then (
                        if !can_perform then (
                            can_perform := false;
                            left := !left + (get_val inst);
                            sol t;
                        ) else ( 
                            can_perform := true;
                            sol lst;
                        )
                    ) else
                        sol t;
            in
            sol l
    ;

    (Common.range 0 (40*6) 40)
        |> List.map ~f:(fun i ->
            let sub = Array.sub ~pos:i ~len:40 img in
            let buf = Buffer.create 40 in
            Array.iter ~f:(Buffer.add_char buf) sub;
            Buffer.contents buf
        )
        |> List.iter ~f:(fun s -> Printf.printf "%s\n" s)
    ;

    (* Separate output *)
    Printf.printf "-------\n";
) inp;;
