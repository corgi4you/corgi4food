import React, {useState} from "react";

function ButtonLoad() {
    const [isLoadingData, setIsLoadingData] = useState(false);
    const [data, setData] = useState([]);
    const [showData, setShowData] = useState(false);

    const handleClick = () => {
        setIsLoadingData(true);
        setShowData(true);
        fetch("/foods/random")
            .then((res) => res.json())
            .then((json) => {
                setIsLoadingData(false);
                setData(json['data'])
                console.log(data)
            })
            .catch((error) => console.log(error));
    };

    return (
        <div>
            <button onClick={handleClick}>Load Data</button>
            {
                showData ? (
                    isLoadingData ? (
                        <h1>Loading...</h1>
                    ) : (
                        <h1>{data.strArea}</h1>
                    )
                ) : (
                    <div></div>
                )
            }
        </div>
    );
}

export default ButtonLoad;