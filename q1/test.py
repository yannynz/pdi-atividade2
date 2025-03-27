import cv2
import numpy as np


def get_dominant_color(hsv_region):
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    lower_orange = np.array([10, 120, 120])
    upper_orange = np.array([25, 255, 255])
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 30, 255])

    mask_red = cv2.bitwise_or(
        cv2.inRange(hsv_region, lower_red1, upper_red1),
        cv2.inRange(hsv_region, lower_red2, upper_red2)
    )

    mask_green = cv2.inRange(hsv_region, lower_green, upper_green)
    mask_orange = cv2.inRange(hsv_region, lower_orange, upper_orange)
    mask_white = cv2.inRange(hsv_region, lower_white, upper_white)

    total_pixels = hsv_region.size / 3
    counts = {
        'red': cv2.countNonZero(mask_red) / total_pixels,
        'green': cv2.countNonZero(mask_green) / total_pixels,
        'orange': cv2.countNonZero(mask_orange) / total_pixels,
        'white': cv2.countNonZero(mask_white) / total_pixels
    }

    return max(counts, key=counts.get)


def identifica_bandeira(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    flags = []

    for contour in contours:
        if cv2.contourArea(contour) < 100:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        roi = img[y:y+h, x:x+w]
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        height, width = hsv_roi.shape[:2]

        aspect_ratio = width / height
        is_vertical = aspect_ratio < 1.2

        country = "unknown"

        if is_vertical:
            segment = width // 3
            left = hsv_roi[:, :segment]
            middle = hsv_roi[:, segment:2*segment]
            right = hsv_roi[:, 2*segment:]

            left_color = get_dominant_color(left)
            middle_color = get_dominant_color(middle)
            right_color = get_dominant_color(right)

            # Peru: Red-White-Red
            if left_color == 'red' and middle_color == 'white' and right_color == 'red':
                country = 'peru'
            # Italy: Green-White-Red
            elif left_color == 'green' and middle_color == 'white' and right_color == 'red':
                country = 'italia'
            # Ireland: Green-White-Orange
            elif left_color == 'green' and middle_color == 'white' and right_color == 'orange':
                country = 'irlanda'

        else:
            segment = height // 2
            top = hsv_roi[:segment, :]
            bottom = hsv_roi[segment:, :]

            top_color = get_dominant_color(top)
            bottom_color = get_dominant_color(bottom)

            if 0.7 <= aspect_ratio <= 0.9:
                if top_color == 'red' and bottom_color == 'white':
                    country = 'monaco'
            elif 0.5 <= aspect_ratio <= 0.8:
                if top_color == 'white' and bottom_color == 'red':
                    country = 'singapura'

        if country != "unknown":
            flags.append((country, (x, y), (x + w, y + h)))

    return flags
