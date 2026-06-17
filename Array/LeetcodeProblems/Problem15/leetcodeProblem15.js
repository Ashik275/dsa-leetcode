function findingTriplets(numbers) {
    const result = [];
    const seen = new Set();
    for (let i = 0; i < numbers.length - 2; i++) {
        for (let j = i + 1; j < numbers.length - 1; j++) {
            for (let k = j + 1; k < numbers.length; k++) {

                const triplet = [numbers[i], numbers[j], numbers[k]];
                const sum = numbers[i] + numbers[j] + numbers[k];
                if (sum === 0) {
                    const key = [...triplet].sort((a, b) => a - b).join(",");
                    console.log(seen);
                    
                    
                    if (!seen.has(key)) {
                        seen.add(key);
                        result.push(triplet);
                    }
                }
            }
        }
    }
    return result;
}


// console.log(
    findingTriplets([-1, 0, 1, 2, -1, -4])
// );