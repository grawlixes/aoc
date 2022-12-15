open Core;;
include Lib;;

Printf.printf "\n";;
Printf.printf "Part 1:\n";;

(* Edit this with the correct day *)
let inp = 
    [Common.read_input "./bin/05/sample.txt";
     Common.read_input "./bin/05/input.txt"]
;;

let lengths = [|3; 9|];;

(* have to comment this out because I have strict unused var checking
let print_stacks stacks =
    stacks
        |> Array.iteri ~f:(fun _ lst ->
            let rec p = function
                | [] -> ()
                | h :: t ->
                    Printf.printf "%c, " h;
                    p t;
            in
            p lst;
            Printf.printf "\n";
        )
;;
*)

let push stacks i el =
    let a = stacks.(i) in
    stacks.(i) <- (el :: a);
;;

let pop stacks i =
    let aux = function
        | [] -> '\n'
        | h :: t ->
            stacks.(i) <- t;
            h
    in
    aux stacks.(i)
;;

(* Part 1 *)
List.iteri ~f:(fun i s ->
    let l = lengths.(i) in
    let stacks = Array.create ~len:l [] in
    let spl = (String.split_on_chars ~on:['\n'] s)
        |> Array.of_list
    in
    let (blank_index, _) = (Array.findi_exn ~f:(fun _ s -> String.length s = 0) spl) in
    
    (* Push the original elements *)
    for ri = (blank_index - 2) downto 0 do
        let row = spl.(ri) in
        for si = 0 to (l - 1) do
            let ch = String.get row (4*si + 1) in
            if not (Char.equal ch ' ') then 
                push stacks si ch;
        done; 
    done;

    (* Do the instructions *)
    for ri = (blank_index + 1) to (Array.length spl - 2) do
        let spl_inst = String.split_on_chars ~on:[' '] (spl.(ri))
            |> Array.of_list
        in
        let count = int_of_string (spl_inst.(1)) in
        let take = int_of_string (spl_inst.(3)) in
        let receive = int_of_string (spl_inst.(5)) in
        for _ = 1 to count do
            (pop stacks (take - 1))
                |> push stacks (receive - 1)
            ;            
        done;
    done;

    (* Build the final string *)
    stacks
        |> Array.fold ~init:"" ~f:(fun acc -> function
            | [] -> acc
            | h :: _ -> acc ^ (String.make 1 h)
        ) 
        |> Printf.printf "%s\n"    
    ;
) inp;;

Printf.printf "\nPart 2:\n";;
(* Part 2 *)
List.iteri ~f:(fun i s ->
    let l = lengths.(i) in
    let stacks = Array.create ~len:l [] in
    let spl = (String.split_on_chars ~on:['\n'] s)
        |> Array.of_list
    in
    let (blank_index, _) = (Array.findi_exn ~f:(fun _ s -> String.length s = 0) spl) in
    
    (* Push the original elements *)
    for ri = (blank_index - 2) downto 0 do
        let row = spl.(ri) in
        for si = 0 to (l - 1) do
            let ch = String.get row (4*si + 1) in
            if not (Char.equal ch ' ') then 
                push stacks si ch;
        done; 
    done;

    (* Do the instructions *)
    for ri = (blank_index + 1) to (Array.length spl - 2) do
        let spl_inst = String.split_on_chars ~on:[' '] (spl.(ri))
            |> Array.of_list
        in
        let count = int_of_string (spl_inst.(1)) in
        let take = int_of_string (spl_inst.(3)) in
        let receive = int_of_string (spl_inst.(5)) in
       
        (* Use supplementary array to maintain order *) 
        let tmp = Array.create ~len:count ' ' in
        for ai = 0 to (count - 1) do
            tmp.(ai) <- pop stacks (take - 1);
        done;

        for ai = (count - 1) downto 0 do
            push stacks (receive - 1) tmp.(ai);
        done;
    done;

    (* Build the final string *)
    stacks
        |> Array.fold ~init:"" ~f:(fun acc -> function
            | [] -> acc
            | h :: _ -> acc ^ (String.make 1 h)
        ) 
        |> Printf.printf "%s\n"    
    ;
) inp;;

Printf.printf "\nPart 2:\n";;
