'''THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND
NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE
DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

# Bitcoin Cash (BCH)   qpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk
# Ether (ETH) -        0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB
# Litecoin (LTC) -     Lfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu
# Bitcoin (BTC) -      34L8qWiQyKr8k4TnHDacfjbaSqQASbBtTd

# contact :- github@jamessawyer.co.uk



"""example of simple chaos machine"""

# Chaos Machine (K, t, m)
K = [0.33, 0.44, 0.55, 0.44, 0.33]
t = 3
m = 5

# Buffer Space (with Parameters Space)
buffer_space, params_space = [], []

# Machine Time
machine_time = 0


def push(seed):
    global buffer_space, params_space, machine_time, K, m, t

    # Choosing Dynamical Systems (All)
    for key, value in enumerate(buffer_space):
        # Evolution Parameter
        e = float(seed / value)

        # Control Theory: Orbit Change
        value = (buffer_space[(key + 1) % m] + e) % 1

        # Control Theory: Trajectory Change
        r = (params_space[key] + e) % 1 + 3

        # Modification (Transition Function) - Jumps
        buffer_space[key] = round(float(r * value * (1 - value)), 10)
        params_space[key] = r  # Saving to Parameters Space

    # Logistic Map
    assert max(buffer_space) < 1
    assert max(params_space) < 4

    # Machine Time
    machine_time += 1


def pull():
    global buffer_space, params_space, machine_time, K, m, t

    # PRNG (Xorshift by George Marsaglia)
    def xorshift(X, Y):
        X ^= Y >> 13
        Y ^= X << 17
        X ^= Y >> 5
        return X

    # Choosing Dynamical Systems (Increment)
    key = machine_time % m

    # Evolution (Time Length)
    for i in range(0, t):
        # Variables (Position + Parameters)
        r = params_space[key]
        value = buffer_space[key]

        # Modification (Transition Function) - Flow
        buffer_space[key] = round(float(r * value * (1 - value)), 10)
        params_space[key] = (machine_time * 0.01 + r * 1.01) % 1 + 3

    # Choosing Chaotic Data
    X = int(buffer_space[(key + 2) % m] * (10 ** 10))
    Y = int(buffer_space[(key - 2) % m] * (10 ** 10))

    # Machine Time
    machine_time += 1

    return xorshift(X, Y) % 0xFFFFFFFF


def reset():
    global buffer_space, params_space, machine_time, K, m, t

    buffer_space = K
    params_space = [0] * m
    machine_time = 0


#######################################

# Initialization
reset()

# Pushing Data (Input)
import random

message = random.sample(range(0xFFFFFFFF), 100)
for chunk in message:
    push(chunk)

# for controlling
inp = ""

# Pulling Data (Output)
while inp in ("e", "E"):
    print("%s" % format(pull(), "#04x"))
    print(buffer_space)
    print(params_space)
    inp = input("(e)exit? ").strip()
