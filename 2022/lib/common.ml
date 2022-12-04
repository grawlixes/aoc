open Core;;

let print_tuple t =
    let (x,y) = t in
    Printf.printf "(%d, %d)\n" x y
;;

let read_input path = 
    In_channel.read_all path
;;

(* Convert a char's literal value to int (0-9) *)
let char_to_int c = 
    (Char.to_int c) - (Char.to_int '0')
;;

(* Get length of list l *)
let rec length = function
    | []     -> 0
    | _ :: t -> 1 + (length t)
;;

(* Maps array a according to function f, then flattens *)
let map_and_flatten a f = 
    List.concat (List.map ~f:f a)
;;

(* Generates a list [i, j) skipping by k *)
let range i j k =
    List.init ((j - i) / k) ~f:(fun x -> (k*x + i))
;;

(* Generates pairs (x, y) for x,y in [i, j) 
 * skipping by k *)
let generate_pairs i j k =
  let gen_range = fun x -> (i + x*k) in
  map_and_flatten (List.init ((j - i) / k) ~f:gen_range)
    (fun a ->
      map_and_flatten (List.init ((j - i) / k) ~f:gen_range)
        (fun b -> [(a, b)])
    )
;;

(* Returns true if all elements in l are true, false otherwise *)
let rec all = function
    | []         -> true
    | false :: _ -> false
    | true :: t  -> all t
;;

(* Returns true if at least one element in l is true, false otherwise *)
let rec any = function
    | []         -> false
    | false :: t -> any t
    | true :: _  -> true
;;

(* Returns a 2d matrix of elements from the given
 * file name. Assumes that newlines split 1d arrays,
 * can optionally provide a split character for 1d
 * arrays and a mapping function. f **MUST TAKE**
 * three inputs, two indices and an element, to make it
 * useful for both cases.
 *)
let read_matrix path delim f =
    let s =
        (In_channel.read_all path)
    in
    (String.split_on_chars ~on:['\n'] s)
        |> List.filter ~f:(fun s ->
            String.length s > 0
        )
        |> List.mapi ~f:(fun i ss ->
            (String.split_on_chars ~on:[delim] ss)
                |> List.mapi ~f:(fun j x -> f i j x)
                |> Array.of_list
        )
        |> Array.of_list
;;
