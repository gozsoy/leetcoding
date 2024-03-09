// ---------------------------------------------------
// 2625. Flatten Deeply Nested Array
// recursion
// time: ?, space: ?

var flat = function (arr, n) {

    let new_arr = []

    function aux(arr, n){
        for (el of arr){
            if (Array.isArray(el) && n>0){
                aux(el, n-1)
            }
            else{
                new_arr.push(el)
            }
        }
    }

    aux(arr, n)
    return new_arr
    
};


// ---------------------------------------------------
// 2705. Compact Object
// recursion

var compactObject = function(obj) {

    function aux(temp_obj){

        if (Array.isArray(temp_obj)){
            let new_arr = []

            for (const el of temp_obj){
                if (Object(el)===el){
                    new_arr.push(aux(el))
                }
                else if (Boolean(el)){
                    new_arr.push(el)
                }
            }

            return new_arr
        }
        else{

            let new_obj = {}

            for (const el in temp_obj){
                if (Object(temp_obj[el])===temp_obj[el]){
                    new_obj[el] = aux(temp_obj[el])
                }
                else if (Boolean(temp_obj[el])){
                    new_obj[el] = temp_obj[el]
                }
            }

            return new_obj
        }

    }

    return aux(obj)

};


// ---------------------------------------------------
// 2694. Event Emitter

class EventEmitter {
    
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */

    d = {}

    subscribe(eventName, callback) {

        if (eventName in this.d){
            this.d[eventName].push(callback)
        }
        else{
            this.d[eventName] = [callback]
        }

        return {
            unsubscribe: () => {

                if (this.d[eventName].length==1){
                    delete this.d[eventName]
                }
                else{

                    let temp_arr = []

                    for (let idx=0;idx<this.d[eventName].length;idx++){
                        
                        if (this.d[eventName][idx]!==callback){
                            temp_arr.push(this.d[eventName][idx])
                        }
                    }

                    this.d[eventName] = temp_arr

                    return

                }
                
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
  
        if (!(eventName in this.d)){
            
            return []
        }

        let results = []
        
        for (const vals of this.d[eventName]){
            let temp = vals(...args)
            results.push(temp)
        }

        return results

    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */


// ---------------------------------------------------
// 2721. Execute Asynchronous Functions in Parallel

var promiseAll = function(functions) {

    return new Promise((resolve, reject) =>{

        let arr = Array(functions.length).fill(0)
        let resolved_cnt = 0

        functions.forEach(async (el, idx) => {
    
            try {
                const res = await el()
                arr[idx] = res
                resolved_cnt++
                
                if (resolved_cnt == functions.length){
                    resolve(arr)
                }
            }
            catch(err) {
                reject(err)
            }

        })

    })
    
};

// ---------------------------------------------------
// 2636. Promise Pool

var promisePool = async function(functions, n) {

    return new Promise((resolve) => {

        let pending_cnt = 0
        let curr_idx = 0

        function aux(){
            
            if (curr_idx >= functions.length){
                if (pending_cnt == 0){
                    resolve()
                }
            }

            while (pending_cnt < n && curr_idx < functions.length){
                
                pending_cnt += 1
                const promise = functions[curr_idx]()
                curr_idx += 1

                promise.then(() =>{
                    pending_cnt-=1
                    aux()
                })
            }

        }
        
        aux()
    })

};

// ---------------------------------------------------
// 2632. Curry

var curry = function(fn) {
    
    let arg_sofar = []
    let total_args = fn.length

    return function curried(...args) {
        
        arg_sofar.push(...args)

        if (total_args == arg_sofar.length){
            return fn(...arg_sofar)
        }
        else{
            return curried
        }

    }
};


// ---------------------------------------------------
// 2628. JSON Deep Equal

var areDeeplyEqual = function(o1, o2) {
    
    // primitive
    if (Object(o1)!==o1){
        if (Object(o2)!==o2 && o1===o2){
            return true
        }
        else{
            return false
        }
    }
    // array
    else if (Array.isArray(o1)){
        if (Array.isArray(o2) && o1.length==o2.length){

            for (let idx=0; idx<o1.length;idx++){
                if(!areDeeplyEqual(o1[idx], o2[idx])){
                    return false
                }
            }

            return true

        }
        else{
            return false
        }

    }
    // object
    else{
        if (!Array.isArray(o2) && Object(o2)===o2  && Object.keys(o1).sort().toString()==Object.keys(o2).sort().toString()){
            
            for (const temp_key in o1){
                if (!areDeeplyEqual(o1[temp_key], o2[temp_key])){
                    return false
                }
            }

            return true          
        }
        else{
            return false
        }

    }

};

// ---------------------------------------------------
// 2676. Throttle

var throttle = function(fn, t) {
    
    let latest_args = null;
    let is_working = null;

    const aux = () => {
        if (latest_args==null){
            is_working=null
        }
        else{
            fn(...latest_args)
            latest_args=null
            is_working=setTimeout(aux, t)
        }
    }

    return function(...args) {
        
        if (!is_working){
            fn(...args)
            is_working = setTimeout(aux, t)
        }
        else{
            latest_args = args
        }
    }
};