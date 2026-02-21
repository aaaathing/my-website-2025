import asyncio
import numpy as np
import sounddevice as sd
import websockets
import threading

SAMPLE_RATE = 2000
BLOCK_SIZE = int(SAMPLE_RATE/20)
WAVE = np.array([1.0, 1.0, -1.0, -1.0], dtype=np.float32)

state = [0.0, 0.0]

lock = threading.Lock()

def audio_callback(outdata, frames, time, status):
    if status:
        print(status)

    with lock:
        volume1, volume2 = state

    wave = np.resize(WAVE, frames)

    outdata[:, 0] = wave * volume1
    outdata[:, 1] = wave * volume2

async def ws_handler(websocket):
    async for message in websocket:
        data = [float(x) for x in message.split(",")]
        global state
        with lock:
            state = data

def find_output_device(name_substring: str) -> int:
    name_substring = name_substring.lower()
    devices = sd.query_devices()

    for i, dev in enumerate(devices):
        if dev["max_output_channels"] > 0:
            if name_substring in dev["name"].lower():
                return i

    raise RuntimeError(f"No output device matching '{name_substring}'")

async def main():
    stream = sd.OutputStream(
        samplerate=SAMPLE_RATE,
        channels=2,
        callback=audio_callback,
        blocksize=BLOCK_SIZE,
        device=find_output_device("phone")
    )
    stream.start()

    async with websockets.serve(ws_handler, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
