import { useEffect, useContext } from "react";
import { GoogleMapContext } from "../context/GoogleMapContext";

const API_KEY = import.meta.env.VITE_REACT_APP_GOOGLE_MAPS_API_KEY;

const useGetCurrentLocation = () => {
  const { setCenter, center } = useContext(GoogleMapContext);

  useEffect(() => {
    const getCurrentLocation = async () => {
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      };

      try {
        const res = await fetch(
          `https://www.googleapis.com/geolocation/v1/geolocate?key=${API_KEY}`,
          requestOptions,
        );
        const data = await res.json();
        setCenter(data.location);
      } catch (error) {
        console.error("Error fetching geolocation:", error);
      }
    };

    getCurrentLocation();
  }, [setCenter]);

  return center;
};

export { useGetCurrentLocation };
