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
// time: ?, space: ?

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