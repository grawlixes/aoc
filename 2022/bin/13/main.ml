open Core;;
include Lib;;

Printf.printf "\n";;
Printf.printf "Part 1:\n";;

(* Edit this with the correct day *)
let inp = 
    [Common.read_input "./bin/13/sample.txt";
     Common.read_input "./bin/13/input.txt"]
;;

type 'a node =
  | One of 'a 
  | Many of 'a node list
;;

let rec build_list s i =
    let l = ref i in
    let res = ref [] in
    while not (Char.equal s.[!l] ']') do
        let j = ref (!l+1) in
        while Option.is_none (List.find ~f:(fun c -> Char.equal c s.[!j]) ['['; ']'])  do
            j := !j + 1;
        done;

        String.sub ~pos:(!l+1) ~len:(!j - !l - 1) s
            |> String.split_on_chars ~on:[',']
            |> List.filter ~f:(fun s -> String.length s > 0)
            |> List.map ~f:(fun s -> One (int_of_string s))
            |> List.iter ~f:(fun v ->
                res := v :: !res;
            )
        ;
          
        if Char.equal s.[!j] '[' then ( 
            let (nxt, k) = build_list s !j in
            res := nxt :: !res;
            l := k + 1;
        ) else
            l := !j; 
    done;
    
    (Many (List.rev !res), !l)
;;

let rec valid (a, b) =
    let extract = function
        | One v -> [One v]
        | Many v -> v
    in
    let left = extract a in
    let right = extract b in
    match (left, right) with
        | ([], []) -> None
        | (_ :: _, []) -> Some false
        | ([], _ :: _) -> Some true
        | (One x :: t1, One y :: t2) ->
            if x < y then
                Some true
            else if x > y then
                Some false
            else
                valid (Many t1, Many t2)
        | (x :: t1, y :: t2) ->
            let tr = valid (x, y) in
            if Option.is_none tr then
                valid (Many t1, Many t2)
            else if Option.value_exn tr then
                Some true
            else
                Some false
;;     

(* Part 1 *)
List.iter ~f:(fun s ->
    (* Code goes here *)
    let ret = ref 0 in
    let inp = String.split_on_chars ~on:['\n'] s
        |> Array.of_list
    in
    Common.range 0 (Array.length inp) 3
        |> List.iter ~f:(fun i ->
            let pair_number = (i / 3) + 1 in
            let (left, _) = build_list inp.(i) 0 in
            let (right, _) = build_list inp.(i+1) 0 in
            ret := !ret + (
                let res = valid (left, right) in
                if Option.is_none res ||
                   (Option.value_exn res) then 
                    pair_number 
                else 
                    0
            )
        )
    ;

    Printf.printf "%d\n" !ret;
    (* Separate output *)
    Printf.printf "-------\n";
) inp;;

Printf.printf "\nPart 2:\n";;
(* Part 2 *)
List.iter ~f:(fun s ->
    (* Code goes here *)
    let inp = String.split_on_chars ~on:['\n'] s
        |> Array.of_list
    in
    let lst = ref [] in
    Common.range 0 (Array.length inp) 3
        |> List.iter ~f:(fun i ->
            let (left, _) = build_list inp.(i) 0 in
            let (right, _) = build_list inp.(i+1) 0 in
            lst := left :: right :: !lst;
        )
    ;

    lst := Many [ Many [ One 2 ] ] :: !lst;
    lst := Many [ Many [ One 6 ] ] :: !lst;

    let a = Array.of_list !lst in
    let comp = fun t1 t2 ->
        let v = valid (t1, t2) in
        if Option.is_none v then
            0
        else if Option.value_exn v then
            -1
        else
            1
    in
    Array.sort ~compare:comp a;

    a
        |> Array.mapi ~f:(fun j v ->
            match v with
                | Many [ Many [ One 2 ] ] -> j+1
                | Many [ Many [ One 6 ] ] -> j+1
                | _ -> 1
        )
        |> Array.fold ~f:(fun acc x -> acc * x) ~init:1
        |> Printf.printf "%d\n"
    ;

    (* Separate output *)
    Printf.printf "-------\n";
) inp;;
